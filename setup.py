import os
import subprocess
import sys
import platform

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running command: {command}")
        print(e)
        sys.exit(1)

def is_docker_running():
    try:
        subprocess.check_call(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def build_nginx_image():
    os.chdir("nginx")
    run_command("docker build -t nginx-proxy .")
    os.chdir("..")

def setup_flask_apps(app_directories):
    for app_dir in app_directories:
        os.chdir(app_dir)
        run_command(f"{sys.executable} -m pip install -r requirements.txt")
        os.chdir("..")

def create_renew_script():
    script_content = """#!/bin/bash
docker run -it --rm --name certbot -v /etc/letsencrypt:/etc/letsencrypt -v /var/www/certbot:/var/www/certbot certbot/certbot renew
docker exec nginx-proxy nginx -s reload
"""
    script_path = "/usr/local/bin/renew_cert.sh"
    with open(script_path, "w") as script_file:
        script_file.write(script_content)
    run_command(f"chmod +x {script_path}")
    return script_path

def create_cron_job(script_path):
    cron_command = f"0 2 * * * {script_path} >> /var/log/renew_cert.log 2>&1"
    run_command(f"(crontab -l ; echo \"{cron_command}\") | crontab -")

def main():
    if not is_docker_running():
        print("Docker n'est pas en cours d'exécution. Veuillez démarrer Docker.")
        sys.exit(1)
    
    # Check if the nginx-proxy image exists
    result = subprocess.run(["docker", "images", "-q", "nginx-proxy"], capture_output=True, text=True)
    if not result.stdout.strip():
        print("L'image nginx-proxy n'existe pas. Création de l'image...")
        build_nginx_image()
    else:
        print("L'image nginx-proxy existe déjà.")

    # Setup Flask applications
    flask_apps = ["app"]
    setup_flask_apps(flask_apps)

    # Create and configure renew script and cron job on Linux
    if platform.system() == "Linux":
        script_path = create_renew_script()
        create_cron_job(script_path)
        print("Cron job pour le renouvellement des certificats SSL a été créé.")
    else:
        print("La création de tâches cron est uniquement prise en charge sur Linux.")

    print("Configuration terminée avec succès.")

if __name__ == "__main__":
    main()
