# import pandas
# import folium
# # From CSV file
# # data = pandas.read_csv('Volcanoes.csv')

# # To CSV file
# # data.to_csv('Pandas_Volcanoes.csv')
# # print(data)
# # print(type(data)) # pandas.core.frame.DataFrame

# # print(data.columns)

# # lat = list(data["LAT"])
# # lon = list(data["LON"]))
# print(dir(help(folium.CircleMarker)))

# import folium
# import pandas as pd
 
# SF_COORDINATES = (37.76, -122.45)
# crimedata = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
 
# # for speed purposes
# MAX_RECORDS = 1000
  
# # create empty map zoomed in on San Francisco
# map = folium.Map(location=SF_COORDINATES, zoom_start=12)
 
# # add a marker for every record in the filtered data, use a clustered view
# for each in crimedata[0:MAX_RECORDS].iterrows():
#     map.simple_marker(
#         location = [each[1]['Y'],each[1]['X']], 
#         clustered_marker = True)
  
# display(map)

import folium
import pandas
 
SF_COORDINATES = (37.76, -122.45)
crimedata = pandas.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
 
# for speed purposes
MAX_RECORDS = 1000
  
# create empty map zoomed in on San Francisco
map = folium.Map(location=SF_COORDINATES, zoom_start=12)
 
# add a marker for every record in the filtered data, use a clustered view
for each in crimedata[0:MAX_RECORDS].iterrows():
    pass
    
display(map)