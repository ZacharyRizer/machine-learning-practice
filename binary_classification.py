# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i9EzeqIddhMwnQRRAxm1sudrzW5wjUla

## Classifying Movie Reviews - _Binary Classification Problem_

Using Tensorflow, Keras, and Matplotlib
"""

from tensorflow.keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)

"""Because only the top 10,000 most frequent words are being used, no word index will exceed 10,000:"""

max([max(sequence) for sequence in train_data])

"""Cleaning the data - turning into 10,000-dimensional vectors of 0s or 1s"""

import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        for j in sequence:
            results[i,j] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)

y_train = np.asarray(train_labels).astype("float32")
y_test = np.asarray(test_labels).astype("float32")

