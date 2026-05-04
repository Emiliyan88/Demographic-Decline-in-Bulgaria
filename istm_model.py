import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_model():
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(1,1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model