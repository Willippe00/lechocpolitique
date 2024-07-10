import ssl
from threading import Thread
from waitress import serve
from app import create_app

app_http = create_app()
app_https = create_app()

def run_http():
    serve(app_http, host='0.0.0.0', port=5000)

def run_https():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('/home/william/Documents/production/lechocpolitique/SSL/certfile.pem', 'C:\Users\willi\Documents\UniWill\projet\lechocpolitique\SSL\keyfile.pem'    serve(app_https, host='0.0.0.0', port=5001, _sock=None, expose_tracebacks=True, threads=8, url_scheme='https', ssl_context = context)

if __name__ == "__main__":
    # Start HTTP server
    http_thread = Thread(target=run_http)
    http_thread.start()

    # Start HTTPS server
    https_thread = Thread(target=run_https)
    https_thread.start()
