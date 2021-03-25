import brickschema   
import rdflib
from rdflib import Namespace
import matplotlib.pyplot as plt
import pandas as pd 


g = brickschema.Graph()
g.load_file("Brick.ttl")
g.load_file("test.ttl")

g.expand("owlrl")


IER = Namespace("http://edificio-test/unamIER#")
g.bind("ier", IER)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

#se manda llamar todos los sensores de un piso especifico
sensor_por_piso = """
SELECT DISTINCT ?equip ?sensor WHERE {
    :floor2 (brick:hasPart|^brick:isPartOf|brick:isLocationOf|^brick:hasLocation)+ ?equip .
    ?equip a/rdfs:subClassOf* brick:RaspberryPi .
    ?equip brick:hasPoint ?sensor .
}
"""
results = g.query(sensor_por_piso)
for row in results:
    print("{}: {}".format(row[0], row[1]))
       
############################################################################################################################################################################################
#se manda llamar el piso especifico junto con el sensor especifico
floor1 = g.query ("""SELECT DISTINCT ?sensor WHERE  { :floor2 (brick:hasPart|^brick:isPartOf|brick:hasPoint|^brick:isPointOf|brick:isLocationOf|^brick:hasLocation)+ ?sensor .  ?sensor a/rdfs:subClassOf* brick:Voltaje_Sensor . } """)

for row in floor1:
    print(row)

