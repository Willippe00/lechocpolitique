import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from waitress import serve

app = create_app()


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)

