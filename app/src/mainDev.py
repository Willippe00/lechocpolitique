from threading import Thread
from waitress import serve
from app import create_app

app_http = create_app()

def run_http():
    serve(app_http, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Start HTTP server
    http_thread = Thread(target=run_http)
    http_thread.start()
