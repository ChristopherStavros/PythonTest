import folium
import pandas

'''
Folium creates web maps
Generates HTML, CSS, Javascript
print(dir(folium))
print(help(folium.Map))
'''

# Get volcanoes from CSV file and create Pandas Data Frame
data = pandas.read_csv('Volcanoes.csv')

# Create lists from columns
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

# Base map
map1 = folium.Map(location=[42, -122], zoom_start=5, tiles="Mapbox Bright")

# Define feature goup
fg = folium.FeatureGroup(name="My Map")

# Add markers to feature group
for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup="{}, {} meters".format(nm, el), icon=folium.Icon(color='green')))
    #NOTE to convert float to a string - popup = folium.Popup(str(el).parse_html=True)

# Add feature group to map
map1.add_child(fg)

# Save map to file
map1.save("Map1.html")

