import tensorflow as tf
from tensorflow.keras.layers import*
from tensorflow.keras.models import Model

def build_unet_model(input_size=(256,256,4)):
    # Input layer
    inputs = Input(input_size)

# Encoder path
conv1 = Conv2D(64,3,activation='relu', padding='same')(inputs)
conv1 = Conv2D(64,3,activation='relu', padding='same')(conv1)
pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

conv2 = Conv2D(128,3,activation='relu', padding='same')(pool1)
conv2 = Conv2D(128,3,activation='relu', padding='same')(conv2)

# Middle
conv3 = Conv2D(256,3,activation='relu', padding='same')(pool2)
conv3 = Conv2D(256,3,activation='relu', padding='same')(conv3)

# Decoder path with skip connections
up1 = UpSampling2D(size=(2, 2))(conv3)
up1 = concatenate([up1, conv2], axis=3)
conv4 = Conv2D(128,3, activation='relu', padding='same')(up1)
conv4 = Conv2D(128,3, activation='relu', padding='same')(conv4)

up2 = UpSampling2D(size=(2, 2))(conv4)
up2 = concatenate([up2, conv1], axis=3)
conv4 = Conv2D(64,3, activation='relu', padding='same')(up2)
conv4 = Conv2D(64,3, activation='relu', padding='same')(conv5)

# Outer layer
outputs = Conv2D(1,1, activation='sigmoid')(conv5)

return Model(inputs=inputs, outputs=outputs)