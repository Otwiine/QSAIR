import geopandas as gpd
import matplotlib.pyplot as plt

# Path to shapefile
file_path = '/Users/otwiine/Desktop/GEO SPATIAL DATA/10m_cultural/10m_cultural/ne_10m_admin_0_countries.shp'

# Reads the shapefile and loads it into a GeoDataFrame.
world = gpd.read_file(file_path)

# print(world.head())
world


ax = world.plot(edgecolor= 'black', color= 'lightgreen')
ax.axis("off")
plt.title('World Map')
plt.show()