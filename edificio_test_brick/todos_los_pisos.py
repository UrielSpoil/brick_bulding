import brickschema   
import rdflib
from rdflib import Namespace
import matplotlib.pyplot as plt
import pandas as pd 



g = brickschema.Graph()
g.load_file("Brick.ttl")
g.load_file("test.ttl")

g.expand("owlrl")

IER = Namespace("http://edificio-test.com/unamIER#")
g.bind("ier", IER)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

#Mandamos llamar todos los pisos
todos_los_pisos = g.query(""" SELECT DISTINCT ?sensor ?floor WHERE 
            { 
                ?sensor rdf:type/rdfs:subClassOf* brick:Location . 
                ?sensor brick:hasPart ?floor . ?floor a brick:Floor . 
             } """)

for row in todos_los_pisos:
    print(row)