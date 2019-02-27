from geopy.geocoders import ArcGIS
gis = ArcGIS()
g = gis.geocode('Italy')
print(g.latitude)
print(g.longitude)
print(g.address)
print(g.altitude)


print(g.value)