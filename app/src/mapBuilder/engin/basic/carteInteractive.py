import folium

#outdir = "C:\Users\willi\Documents\UniWill\projet\lechocpolitique\rst\map"

def buildMap():
    print("creation de carte")
    m = folium.Map(location=(45.5236, -122.6750))
    m.save("./rst/map/cartevierge.html")

