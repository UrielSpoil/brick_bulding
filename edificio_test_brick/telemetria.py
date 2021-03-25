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

df = pd.read_csv("lectura_datos/sensor_amperaje_piso1_pasillo.csv")



############################################################################################################################################################################################
#manda llamar toda la telemetria de un sensor en especifico con grafica
telemetria_sensor_especifico = """ 
SELECT DISTINCT ?equip ?sensor ?csvfile   WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Air_Temperature_Sensor .  
    ?equip a/rdfs:subClassOf* brick:RaspberryPi .
    ?equip brick:hasPoint ?sensor .
    ?sensor brick:timeseries/brick:hasCSVfile ?csvfile 

} """

results = g.query(telemetria_sensor_especifico)
tmp = []
for row in results:
    df = pd.read_csv('lectura_datos/' + row[2], index_col=0, parse_dates=True)
    df = df.resample('60S').mean()
    tmp.append(df)
    print(df)
tmp = pd.concat(tmp, axis=1)
tmp.plot(subplots = True)
plt.show()


############################################################################################################################################################################################
#manda llamar toda la telemetria de un sensor en especifico sin grafica
telemetria_sensor_especifico = g.query(""" SELECT DISTINCT ?sensor ?csvfile  WHERE { ?sensor rdf:type/rdfs:subClassOf* brick:Relative_Humidity_Sensor .  ?sensor brick:timeseries/brick:hasCSVfile ?csvfile } """)

for row in telemetria_sensor_especifico:
    filename = row[1]        
    df = pd.read_csv("lectura_datos/" + filename)
    print(df)

print(row)


############################################################################################################################################################################################
#se manda llamar toda la telemetria de un piso especifico y muestra las graficas
telemetria_por_piso_sensor = """
SELECT DISTINCT ?equip ?sensor ?csvfile WHERE {
    :floor2 (brick:hasPart|^brick:isPartOf|brick:isLocationOf|^brick:hasLocation)+ ?equip .
    ?equip a/rdfs:subClassOf* brick:RaspberryPi .
    ?equip brick:hasPoint ?sensor .
    ?sensor brick:timeseries/brick:hasCSVfile ?csvfile .
}
"""
results = g.query(telemetria_por_piso_sensor)
tmp = []
for row in results:
    df = pd.read_csv('lectura_datos/' + row[2], index_col=0, parse_dates=True)
    df = df.resample('60S').mean()
    tmp.append(df)
    print(df)
tmp = pd.concat(tmp, axis=1)
tmp.plot(subplots = True)
plt.show()

############################################################################################################################################################################################
#se manda llamar todos los sensores de todos los pisos pero con su archivo csv correspondiente 
sensores_con_archivos_csv = """
SELECT DISTINCT ?equip ?sensor ?csvfile WHERE {
    :floor1 (brick:hasPart|^brick:isPartOf|brick:isLocationOf|^brick:hasLocation)+ ?equip .
    ?equip a/rdfs:subClassOf* brick:RaspberryPi .
    ?equip brick:hasPoint ?sensor .
    ?sensor brick:timeseries/brick:hasCSVfile ?csvfile .
}
"""
results = g.query(sensores_con_archivos_csv)
for row in results:
    print("{}: {} {}".format(row[0], row[1], row[2]))









