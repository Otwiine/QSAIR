import rasterio 
import matplotlib.pyplot as plt

# Load the population density raster file
with rasterio.open('/Users/otwiine/Desktop/uga-popugapppv2b2015unadj/UGA_ppp_v2b_2015_UNadj.tif') as src:
      # Read the first band (population density)
      population_density = src.read(1)

# Display the population density as a heatmap
plt.imshow(population_density, cmap='viridis')
plt.show()