from geopy.geocoders import ArcGIS
gis = ArcGIS()
g = gis.geocode('2113 County Road E East 55110')
print(g.latitude)
print(g.longitude)
print(g.address)
print(g.altitude)
