import rasterio
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load multi-band satellite image
with rasterio.open('satellite_image.tif') as src:
    satellite_data = src.read()
    # Reshape to (pixels, bands)
    bands, height, width = satellite_data.shape
    flat_data = satellite_data.reshape(bands, height * width).T

# Load labeled grouped ground truth data
with rasterio.open('crop_labels.tif') as src:
    labels = src.read(1).flatten()

# Filter valid data points (non-zero labels)
valid_pixels = labels > 0
X = flat_data[valid_pixels]
Y = labels[valid_pixels]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

# Train Random Forest model
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_split=10,
    n_jobs=-1,
    random_state=42
    )
rf_model.fit(X_train,y_train)

# Predict on entire image
prediction = np.zeros(height * width,dtype=np.unit8)
prediction[valid_pixels] = rf_model.predict(X)
crop_map = prediction.reshape(height, width)