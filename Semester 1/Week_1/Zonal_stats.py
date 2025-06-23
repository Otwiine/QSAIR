import geopandas as gpd
from rasterstats import zonal_stats
import rasterio 

land_use_gdf = gpd.read_file('/Users/otwiine/Desktop/uganda_other_landuse_type2006/Uganda_Other Land type without populated area2006.shp')

raster_path = '/Users/otwiine/Desktop/uga-popugapppv2b2015unadj/UGA_ppp_v2b_2015_UNadj.tif'

with rasterio.open(raster_path) as src:
    if land_use_gdf.crs != src.crs:
        land_use_gdf = land_use_gdf.to_crs(src.crs)
      
# Calculate zonal statistics for each land use category
zonal_stats_results = zonal_stats(land_use_gdf, raster_path, stats=['mean'])


# Extract the average population density for each land use category
average_density = [stat['mean'] for stat in zonal_stats_results]

print("Average Population Density by Land Use Category:", average_density)