from flask import current_app as app, render_template
from flask import Flask, send_file
from flask import Flask, render_template, request, send_file
import os

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carte')
def carte():
    return render_template('cartevierge.html')

@app.route('/carteStandAlone') #http://localhost:5000/carteStandAlone?map=cartevierge
def carteStandAlone():
    # Obtenir le paramètre de requête pour sélectionner la carte
    map_name = request.args.get('map', 'cartevierge')  # Par défaut 'map1'
    map_file = f'{map_name}.html'
    
    map_path = os.path.join(r'../rst/map', map_file)
    # except:
    #     map_path = os.path.join(r'/home/william/Documents/production/lechocpolitique/app/rst/map', map_file)
    print(map_path)

    if not os.path.exists(map_path):
        map_path = os.path.join(r'/home/william/Documents/production/lechocpolitique/app/rst/map', map_file)
        if not os.path.exists(map_path):
            return "Carte non trouvée", 404
    print("avant render")

    with open(map_path, 'r', encoding='utf-8') as file:
        map_content = file.read()
    return render_template('carte.html', map_file=map_file, map_content=map_content)

@app.route('/logo')
def logo():
    # Assurez-vous que l'image est dans le répertoire "static/images/"
    image_path = r'C:\Users\willi\Documents\UniWill\projet\lechocpolitique\app\rst\image\logo\image.png'

    if not os.path.exists(image_path):
        image_path = r'../rst/image/logo/image.png'
        if not os.path.exists(image_path):
            return "Carte non trouvée", 404
    return send_file(image_path, mimetype='image/png')
