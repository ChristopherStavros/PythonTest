import folium
import pandas

map1 = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
data = pandas.read_csv('Volcanoes.csv')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
html = """
<div>
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
<img src="http://labelme.csail.mit.edu/Release3.0/Images/users/antonio/static_sun_database/v/volcano/sun_aciogupxrimayjmk.jpg"
</div>
"""

# Volcanoes
fgv = folium.FeatureGroup(name="Volcanoes")
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'orange'
    else:
        return 'red'

# for lt, ln, el, name in zip(lat, lon, elev, name):
#     iframe = folium.IFrame(html=html % (name, name, el), width=600, height=400)
#     fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m", 
#     fill_color=color_producer(el), color = 'color_producer(el)', fill_opacity = 0.7))

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 20, popup="Steez",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

    #fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe, max_width = 600), icon=folium.Icon(color=color_producer(el))))

# Population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Finalize and save
map1.add_child(fgv)
map1.add_child(fgp)
map1.add_child(folium.LayerControl())
map1.save("Map1.html")

