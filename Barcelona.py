# From Geopandas Course
import geopandas as gpd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'

districts = gpd.read_file(url)

print(districts.columns) # To show the colum names
print(districts.head(10))
ax = districts.plot(figsize=(10,6), column='DISTRICTE', edgecolor='black', legend=True)

plt.title("Districts of Barcelona", fontsize=12)
plt.axis('off')
plt.show()

# Add district name labels at the centroid of each district
# for x, y, label in zip(districts.geometry.centroid.x, districts.geometry.centroid.y, districts['NOM']):
# ax.text(x, y, label, fontsize=8, ha='center', color='black', fontweight='bold')
