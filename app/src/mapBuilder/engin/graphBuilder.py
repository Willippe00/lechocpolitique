import os
import sys

# Obtenir le chemin du répertoire supérieur
up_Dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ajouter le répertoire supérieur au chemin de recherche de Python
sys.path.append(up_Dir)

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'basic'))
sys.path.append(src_path)

from GraphEnum import GraphName

from carteInteractive import buildMap





class graphBuilder():

    def buildGraph(self, graphToBuild):
        if graphToBuild == GraphName.CARTEVIERGE:
            buildMap()
