import gmaps, gmaps.datasets
from ipywidgets.embed import embed_minimal_html

with open('/home/hansgruber/secrets/google_travel_api_key.txt') as f:
    api_key = f.readline()
    f.close

api_key
gmaps.configure(api_key=api_key)

# Get the dataset
earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')

#Get the locations from the data set
locations = earthquake_df[['latitude', 'longitude']]

#Get the magnitude from the data
weights = earthquake_df['magnitude']

#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
embed_minimal_html('export.html', views=[fig])