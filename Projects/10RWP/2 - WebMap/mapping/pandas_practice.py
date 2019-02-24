import pandas

# From CSV file
data = pandas.read_csv('Volcanoes.csv')

# To CSV file
# data.to_csv('Pandas_Volcanoes.csv')
print(data)
# print(type(data)) # pandas.core.frame.DataFrame

# print(data.columns)

# lat = list(data["LAT"])
# lon = list(data["LON"])