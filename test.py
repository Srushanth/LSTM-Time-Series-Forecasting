import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(input_shape=(4, 1), activation='relu', return_sequences=True)
])