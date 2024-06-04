# To silence tensorflow annoying messages/logs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Importing required libraries and APIs
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

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
train_images = train_images.reshape(-1, 28*28).astype('float32') / 255.0
test_images = test_images.reshape(-1, 28*28).astype('float32') / 255.0

# Build the model using Sequential API

# First way of using Sequential API
model = keras.Sequential(
    [
        keras.Input(shape=(28*28)),
        layers.Dense(512, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(10, activation='softmax'),
    ]
)

# Second way of using Sequential API

# The advantage being you can print(model.summary()) 
# in betwen to see each layer unlike the first where 
# you can only do that after fitting/training the model
# - Helpful for debugging
'''
model = keras.Sequential()
model.add(keras.Input(shape=(28*28)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))
'''

# Compile the model
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
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

# Plot the first 10 test images, their predicted labels, and the true labels
# Color correct predictions in green, incorrect predictions in red
plt.figure(figsize=(15, 5))  # Increase the figure size for 10 images
for i in range(10):  # Change the range to 10
    plt.subplot(2, 5, i + 1)  # Change the subplot layout to 2 rows and 5 columns
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28, 28), cmap=plt.cm.binary)  # Reshape to 28x28
    predicted_label = tf.argmax(predictions[i]).numpy()
    true_label = test_labels[i]
    color = 'green' if predicted_label == true_label else 'red'
    plt.xlabel(f'{predicted_label}', color=color)
plt.tight_layout()
plt.show()
