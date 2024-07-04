from flask import Flask
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    with app.app_context():
        # Importer les routes
        from . import routes

    return app
