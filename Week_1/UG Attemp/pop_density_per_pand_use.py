import rasterio
from rasterio.mask import mask

land_use_gdf = ('/Users/otwiine/Desktop/uganda_other_landuse_type2006/Uganda_Other Land type without populated area2006.shp')

# Load the population density raster file
with rasterio.open('population_density.tif') as src:
      
# Calculate zonal statistics for each land use category
    zonal_stats = rasterio.features.zonal_stats(src.read(1),land_use_gdf.geometry, stats=['mean'])
# Extract the average population density for each land use category
average_density = [stat['mean'] for stat in zonal_stats]