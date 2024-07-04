from flask import current_app as app, render_template
from flask import Flask, send_file

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carte')
def carte():
    return render_template('cartevierge.html')

@app.route('/logo')
def logo():
    # Assurez-vous que l'image est dans le répertoire "static/images/"
    image_path = '..\..\\rst\image\logo\image.png'
    return send_file(image_path, mimetype='image/png')
