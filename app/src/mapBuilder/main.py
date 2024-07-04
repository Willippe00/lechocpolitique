import os
import sys

# Ajouter le répertoire 'src' au chemin de recherche
src_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(src_path)

from GraphEnum import GraphName
from engin.graphBuilder import graphBuilder


if __name__ == "__main__":
    print("hello world")

    
    builder = graphBuilder()
    builder.buildGraph(GraphName.CARTEVIERGE)
    