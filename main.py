"""
FelipelosH

Represetate a Peru in standard to show in Oracle data visualization MAP.json

{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [125.6, 10.1]
  },
  "properties": {
    "name": "Dinagat Islands"
  }
}

based on
https://en.wikipedia.org/wiki/GeoJSON

"""

f = open('turismoi.csv', 'r', encoding="UTF-8")
f = f.read()

finalData = {}

header0 = "{ \"type\": \"FeatureCollection\", \"features\": [\n  "

struct0 = "{\n \"type\": \"Feature\",\n \"geometry\": {\n  \"type\": \"Point\",\n  \"coordinates\": ["

struct1 = "]\n  },\n  \"properties\": {\n  \"name\": \""

struct2 = "\"\n  }\n  }"


for i in f.split("\n")[1:-1]:
    data = i.split("|")
    # Only PE
    if data[1] == "PE":
        city_name = data[9]
        city_lat = "-12.0666"
        city_lng = "-77.0666"
        if data[15] != "NULL":
            city_lat = data[15]
        if data[16] != "NULL":
            city_lng = data[16]
        
        finalData[city_name] = city_lng+","+city_lat



txtToJson = ""


for i in finalData: 
    txtToJson = txtToJson + struct0 + finalData[i] + struct1 + i + struct2 + ",\n"

# Delete las comma and break line
txtToJson = txtToJson[0:-2]
txtToJson = header0 + txtToJson + "\n]}"




f = open('peru.geojson', 'w', encoding="UTF-8")
f.write(txtToJson)
f.close()

