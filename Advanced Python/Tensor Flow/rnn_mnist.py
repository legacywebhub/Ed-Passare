# To silence tensorflow annoying messages/logs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Importing required libraries and APIs
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist

'''
# This line if having GPU issues
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
'''

# Loading the dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)  # (60000, 28, 28) 28*28 are dimensions of the image
print(train_labels.shape)  # (6000,)

# Preprocess the data
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Build the model using Sequential API
model = keras.Sequential()
model.add(keras.Input(shape=(None, 28)))
model.add(layers.SimpleRNN(256, return_sequences=True, activation='tanh'))
model.add(layers.SimpleRNN(256, activation='tanh'))
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(lr=0.001),
    metrics=["accuracy"],
)

# Train the model
model.fit(train_images, train_labels, batch_size=32, epochs=5, verbose=2)

# Model summary
print(model.summary())

# Evaluate the model
model.evaluate(test_images, test_labels, batch_size=32, verbose=2)

# Make predictions
predictions = model.predict(test_images)