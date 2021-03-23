import brickschema   
from rdflib import Namespace


g = brickschema.Graph()
g.load_file("Brick.ttl")
g.load_file("test.ttl")

g.expand("owlrl")

IER = Namespace("http://edificio-test.com/unamIER#")
g.bind("ier", IER)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

pisos_cuartos = g.query(""" SELECT DISTINCT ?sensor ?floor ?building WHERE 
            { 
                ?sensor brick:hasPart ?building . ?floor1 a brick:Floor . 
             } """)

for row in pisos_cuartos:
    
    print(row)

len(pisos_cuartos)