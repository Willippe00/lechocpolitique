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

def start_flask_apps(app_directories):
    for app_dir in app_directories:
        os.chdir(app_dir)
        run_command(f"{sys.executable} src/main.py")
        os.chdir("..")

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

    # Start Flask applications
    flask_apps = ["app"]
    start_flask_apps(flask_apps)

    # Start Nginx container
    run_command("docker run -d --name nginx-proxy -p 80:80 -p 443:443 nginx-proxy")

    print("Toutes les applications Flask et le conteneur Nginx ont démarré avec succès.")

if __name__ == "__main__":
    main()
