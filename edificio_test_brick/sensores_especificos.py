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

#Mandamos llamar el sensor especifico de todos los pisos con su id

temperatura = g.query(""" SELECT DISTINCT ?sensor ?room ?id ?token WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Temperature_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)
for row in temperatura:
    print(row)

#humedad = g.query(""" SELECT DISTINCT ?sensor  ?room ?id ?token WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Relative_Humidity_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)
    #for row in humedad:
    #    print(row)
    
#luminocidad = g.query(""" SELECT DISTINCT ?sensor ?room ?id ?token WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Luminance_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)
    #for row in luminocidad:
    #   print(row)
    
#sonido = g.query(""" SELECT DISTINCT ?sensor ?room ?id ?token WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Sound_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)
    
#for row in sonido:
#    print(row)

#voltaje = g.query(""" SELECT DISTINCT ?sensor ?room ?id ?token WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Voltaje_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)
#for row in voltaje:
#    print(row)

#amperaje = g.query(""" SELECT DISTINCT ?sensor ?room ?id ?token WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Electric_Current_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)
#for row in amperaje:
#    print(row)

nivel_agua = g.query(""" SELECT DISTINCT ?sensor ?room ?id ?token   WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Water_Volumen_Sensor . ?sensor brick:isPointOf ?room . ?room a brick:Room . ?sensor brick:timeseries/brick:hasTimeseriesId ?id . ?sensor brick:timeseries/brick:hasToken ?token } """)

for row in nivel_agua:
    print(row)

    

    









############################################################################################################################################################################################   
#todos_los_sensores = g.query(""" SELECT DISTINCT ?sensor ?floor WHERE 
#                 { 
#                    ?sensor brick:isPointOf ?floor . ?floor1 a brick:Floor . 
#                 } """)

#for row in todos_los_sensores:
#    print(row)

############################################################################################################################################################################################
#todos_los_pisos = g.query(""" SELECT DISTINCT ?sensor ?floor WHERE 
#            { 
#                ?sensor rdf:type/rdfs:subClassOf* brick:Location . 
#                ?sensor brick:hasPart ?floor . ?floor a brick:Floor . 
#             } """)

#for row in todos_los_pisos:
#    print(row)
    
############################################################################################################################################################################################
#pisos_cuartos = g.query(""" SELECT DISTINCT ?sensor ?floor ?building WHERE 
#            { 
#                ?sensor brick:hasPart ?building . ?floor1 a brick:Floor . 
#             } """)

#for row in pisos_cuartos:
#    print(row)
############################################################################################################################################################################################

#floor1 = g.query("""SELECT DISTINCT ?sensor WHERE 
#    {
#       :floor1 (brick:hasPart|^brick:isPartOf|brick:hasPoint|^brick:isPointOf|brick:isLocationOf|^brick:hasLocation)+ ?sensor .  ?sensor a/rdfs:subClassOf* brick:Sensor .
#    } """)

#for row in floor1:
#    print(row)
