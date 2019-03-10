import folium
import pandas
from folium.plugins import MarkerCluster
from geopy.geocoders import ArcGIS


gis = ArcGIS()
g = gis.geocode('Minnesota')
circle = {
    'radius': 7, 'fill':True,'color':'grey', 'fill_opacity':0.7
}
map1 = folium.Map(location=[g.latitude, g.longitude], zoom_start=7)

fgp = folium.FeatureGroup(name="Stuff")
fgp2 = folium.FeatureGroup(name="Stuff2")
mc = MarkerCluster()
g = gis.geocode('2113 COunty Road E East, 55110')
fgp.add_child(folium.CircleMarker(location=[g.latitude, g.longitude], fill_color = 'blue', popup = 'Multi', **circle))
addresses = ['Duluth', '2113 COunty Road E East, 55110', '2113 COunty Road E East , 55110', '2113 COunty Road E East , 55110', '2007 COunty Road E East , 55110']

g = gis.geocode('2113 COunty Road E East, 55110')
fgp2.add_child(folium.CircleMarker(location=[g.latitude, g.longitude], fill_color = 'blue', popup = 'Multi', **circle))
addresses = ['Duluth', '2113 COunty Road E East, 55110', '2113 COunty Road E East , 55110', '2113 COunty Road E East , 55110', '2007 COunty Road E East , 55110']

num = 0
for a in addresses:
    num = num + 1
    if num == 2:
        color = 'green'
    else:
        color = 'black'

    g = gis.geocode(a)
    fgp.add_child(folium.CircleMarker(location=[g.latitude, g.longitude], fill_color = color, popup = "{}, {}".format(a,num), **circle))

num = 0
for a in addresses:
    num = num + 1
    if num == 2:
        color = 'green'
    else:
        color = 'black'

    g = gis.geocode(a)
    fgp2.add_child(folium.CircleMarker(location=[g.latitude, g.longitude], fill_color = color, popup = "{}, {}".format(a,num), **circle))


mc.add_child(fgp)
mc.add_child(fgp2)
# for lt, ln, el in zip(lat, lon, elev):
#     fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 20, popup="Steez",
#     fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

    #fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe, max_width = 600), icon=folium.Icon(color=color_producer(el))))

# Population
# fgp = folium.FeatureGroup(name="Counties")
# fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
# style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
# else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Finalize and save
map1.add_child(mc)
map1.add_child(folium.LayerControl())
map1.save("Map4.html")

