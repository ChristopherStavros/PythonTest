import folium
import folium.plugins
import pandas
from geopy.geocoders import ArcGIS
addresses = ['Minnesota','Duluth', 'Duluth', 'Duluth','Minneapolis', 'Minneapolis', 'Minneapolis', 'Rochester, MN', 'Rochester, MN']
gis = ArcGIS()
g = gis.geocode(addresses[0])
circle = {'radius': 7, 'fill':True,'color':'grey', 'fill_opacity':0.7}

map = folium.Map(location=[g.latitude, g.longitude], zoom_start=6)

markerClusterGroup = folium.plugins.MarkerCluster(control=False, options={'spiderfyDistanceMultiplier': 2})
map.add_child(markerClusterGroup)

groups = {}
names = ["Group1", "Group2"]
colors = ['green', 'blue']
for n, c in zip(names, colors):
    groups[n] = {'group': folium.plugins.FeatureGroupSubGroup(markerClusterGroup, n), 'color': c}
    map.add_child(groups[n]['group'])

    for a in addresses[1:]:
        g = gis.geocode(a)
        groups[n]['group'].add_child(folium.CircleMarker(location=[g.latitude, g.longitude], fill_color = groups[n]['color'], popup = a, **circle))



folium.LayerControl().add_to(map)
map.save("Map5.html")