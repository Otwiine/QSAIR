import geopandas as gpd
import matplotlib.pyplot as plt

# Load the land use shapefile
land_use_gdf = gpd.read_file('/Users/otwiine/Desktop/uganda_other_landuse_type2006/Uganda_Other Land type without populated area2006.shp')

# Inspect GeoDataFrame
print(land_use_gdf.head())

# Visualize the land use patterns
land_use_gdf.plot(column='FTYPE', legend=True)
plt.show()