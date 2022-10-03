import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, utils
import tensorflow_hub as hub
from tensorflow import keras
from tensorflow.keras.models import load_model
import tensorflow_io as tfio

yamnet_model_handle = "https://tfhub.dev/google/yamnet/1"
yamnet_model = hub.load(yamnet_model_handle)
# Please put your the directory where your model is saved below.
# model = keras.models.load_model("C:/Users/MAKTAB/Documents")
# print(os.getcwd())
model = keras.models.load_model("./utils/models/my_model.hdf5")


def load_wav_16k_mono(filename):
    """Load a WAV file, convert it to a float tensor, resample to 16 kHz single-channel audio."""
    # file_contents = tf.io.read_file(filename)
    file_contents = filename
    wav, sample_rate = tf.audio.decode_wav(file_contents, desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tfio.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    if len(wav) < 48000:
        return
    centre = len(wav) // 2
    return wav[(centre - 24000) : (centre + 24000)]


def extract_embedding(wav_data):
    # run YAMNet to extract embedding from the wav data
    scores, embeddings, spectrogram = yamnet_model(wav_data)
    return embeddings


def predict(filename):
    classes = [
        "blues",
        "classical",
        "country",
        "disco",
        "hiphop",
        "jazz",
        "metal",
        "pop",
        "qawwali",
        "reggae",
        "rock",
    ]
    data = load_wav_16k_mono(filename)
    if data == None:
        return
    data = extract_embedding(data)
    data = np.array(data)
    data = data[0:6]
    data = data.reshape(1, 6144)
    predicted_label = model.predict(data)
    classes_x = int(np.argmax(predicted_label, axis=1))
    prediction_class = classes[classes_x]
    return prediction_class


if __name__ == "__main__":
    print(predict("metal.0.wav"))
    print(predict("country.0.wav"))
    print(predict("disco.0.wav"))
