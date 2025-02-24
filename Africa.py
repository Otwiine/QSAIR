import geopandas as gpd
import matplotlib.pyplot as plt

file_path = '/Users/otwiine/Desktop/GEO SPATIAL DATA/10m_cultural/10m_cultural/ne_10m_admin_0_countries.shp'

world = gpd.read_file(file_path)

# Filters the world GeoDataFrame to include only the countries from Africa and stores the data in a new GeoDataFrame called africa
africa = world[world['CONTINENT'] == 'Africa']

# Prints the first 5 rows of the GeoDataFrame
# print(africa.head())
africa

africa.plot(edgecolor='black', color='lightgreen')
plt.title('Map of African Countries')
plt.show()