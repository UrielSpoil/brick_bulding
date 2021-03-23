import brickschema   
from rdflib import Namespace
import pandas as pd 

df = pd.read_csv("lectura_datos/sensor_amperaje_piso1_pasillo.csv")


g = brickschema.Graph()
g.load_file("Brick.ttl")
g.load_file("test.ttl")

g.expand("owlrl")

IER = Namespace("http://edificio-test/unamIER#")
g.bind("ier", IER)

BRICK = Namespace("https://brickschema.org/schema/Brick#")
g.bind("brick", BRICK)

#se manda llamar todos los sensores de un piso especifico
floor1 = g.query("""SELECT DISTINCT ?sensor WHERE  { :floor1 (brick:hasPart|^brick:isPartOf|brick:hasPoint|^brick:isPointOf|brick:isLocationOf|^brick:hasLocation)+ ?sensor .  ?sensor a/rdfs:subClassOf* brick:Sensor . } """)

for row in floor1:
    print(row)
    
############################################################################################################################################################################################
#se manda llamar el piso especifico junto con el sensor especifico
floor1 = g.query ("""SELECT DISTINCT ?sensor WHERE  { :floor2 (brick:hasPart|^brick:isPartOf|brick:hasPoint|^brick:isPointOf|brick:isLocationOf|^brick:hasLocation)+ ?sensor .  ?sensor a/rdfs:subClassOf* brick:Sound_Sensor . } """)

for row in floor1:
    print(row)

############################################################################################################################################################################################
#manda llamar toda la telemetria de un sensor en especifico
#csvFile = g.query(""" SELECT DISTINCT ?sensor ?csvfile  WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Sound_Sensor .  ?sensor brick:timeseries/brick:hasCSVfile ?csvfile } """)

#for row in csvFile:
#    filename = row[1]        
#    df = pd.read_csv("lectura_datos/" + filename)
#    print(df)

#print(row)

#se manda llamar toda la telemetria de un piso especifico
csvFile = g.query("""SELECT DISTINCT ?sensor ?csvfile  WHERE 
    {
       :floor1 (brick:hasPart|^brick:isPartOf|brick:hasPoint|^brick:isPointOf|brick:isLocationOf|^brick:hasLocation)+ ?sensor .  ?sensor a/rdfs:subClassOf* brick:Sensor .  ?sensor brick:timeseries/brick:hasCSVfile ?csvfile } """)

for row in csvFile:
    filename = row[1]        
    df = pd.read_csv("lectura_datos/" + filename)
    print(df)

print(row)