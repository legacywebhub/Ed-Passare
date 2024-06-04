# To silence tensorflow annoying messages/logs
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Importing required libraries and APIs
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

# Preprocess the data
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Build the model using Sequential API
model = keras.Sequential(
    [
        keras.Input(shape=(32, 32, 3)),  # we are maintaining the dimensions and the 3 channels - RGB
        layers.Conv2D(32, (3, 3), padding='valid', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), padding='valid', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(128, (3, 3), padding='valid', activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10)
    ]
)

# Compile the model
model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(learning_rate=3e-4),
    metrics=["accuracy"],
)

# Train the model
model.fit(train_images, train_labels, batch_size=64, epochs=5, verbose=2)

# Model summary
print(model.summary())

# Evaluate the model
model.evaluate(test_images, test_labels, batch_size=64, verbose=2)

# Make predictions
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Define the class names
class_names = ["airplane", "automobile", 
"bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

# Plot the first 10 test images, their predicted labels, and the true labels
plt.figure(figsize=(20, 10))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i])
    predicted_label = class_names[predicted_labels[i]]
    true_label = class_names[test_labels[i][0]]
    color = 'green' if predicted_label == true_label else 'red'
    plt.xlabel(f"{predicted_label}\n({true_label})", color=color)
plt.show()