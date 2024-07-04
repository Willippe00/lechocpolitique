import sys
import os
import ssl

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from waitress import serve


from flask import Flask, request, redirect

app = create_app()

# @app.before_request
# def before_request():
#     if not request.is_secure:
#         return redirect(request.url.replace("http://", "https://", 1))


if __name__ == "__main__":
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    #context.load_cert_chain('/path/to/your/certfile.pem', '/path/to/your/keyfile.pem')
    #serve(app, host='0.0.0.0', port=5001, ssl_context=context)
    serve(app, host='0.0.0.0', port=5002)
