
import tensorflow as tf
import os
from os import walk
import numpy as np
from sklearn.model_selection import KFold

def listing_path(katalog):
    for (dirpath, katalogi, pliki) in walk(katalog):
        break
    return katalogi, pliki

def load_and_preprocess_image(path, label):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [32, 32])  # Dostosuj rozmiar do potrzeb
    image /= 255.0  # Normalizacja
    return image, label


def get_data_with_label(path, label):
    _, files = listing_path(path)
    files = [f"{path}{x}" for x in files]
    label = [label]*len(files)
    return files, label


def get_datasets(image_paths, labels):
    dataset = tf.data.Dataset.from_tensor_slices((image_paths, labels))
    dataset = dataset.map(load_and_preprocess_image)
    dataset = dataset.shuffle(buffer_size=len(image_paths))
    dataset = dataset.batch(4)
    return dataset


bike_train_files, bike_train_label =  get_data_with_label('Dataset/Bike_train/',1)
car_train_files, car_train_label =  get_data_with_label('Dataset/Car_train/',0)
bike_test_files, bike_test_label =  get_data_with_label('Dataset/Bike_test/',1)
car_test_files, car_test_label =  get_data_with_label('Dataset/Car_test/',0)

all_files = bike_train_files + car_train_files + bike_test_files + car_test_files
all_labels = bike_train_label + car_train_label + bike_test_label + car_test_label
all_labels = np.array(all_labels)


nr = np.arange(len(all_labels))
np.random.shuffle(nr)
all_files = [all_files[i] for i in nr]
all_labels = [all_labels[i] for i in nr]



kf = KFold(n_splits=5)
for i, (train_index, test_index) in enumerate(kf.split(all_labels, )):
    train_files = [all_files[i] for i in train_index]
    test_files = [all_files[i] for i in test_index]
    train_labels = [all_labels[i] for i in train_index]
    test_labels = [all_labels[i] for i in test_index]

    train_ds = get_datasets(train_files, train_labels)
    val_ds = get_datasets(test_files, test_labels)
#


    num_classes = 2
    img_height = 32
    img_width = 32


    model = tf.keras.Sequential([
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Conv2D(32, 3, activation='relu'),
      tf.keras.layers.MaxPooling2D(),
      tf.keras.layers.Flatten(),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dense(num_classes)
    ])

    model.compile(
      optimizer='adam',
      loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
      metrics=['accuracy'])


    model.fit(
      train_ds,
      validation_data=val_ds,
      epochs=40
    )



