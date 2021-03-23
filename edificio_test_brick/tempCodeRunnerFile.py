floor1 = g.query("""SELECT DISTINCT ?sensor WHERE 
    {
       :floor1 (brick:hasPart|^brick:isPartOf|brick:hasPoint|^brick:isPointOf|brick:isLocationOf|^brick:hasLocation)+ ?sensor .  ?sensor a/rdfs:subClassOf* brick:Sensor .
    } """)

for row in floor1:
    print(row)