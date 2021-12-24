import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras import regularizers


def predict(chats):
    max_words = 200
    max_len = 200
    tokenizer = Tokenizer(num_words=max_words)
    model = keras.models.load_model(filepath='model.h5', compile=False)
    tokenizer.fit_on_texts(chats)
    sequences = tokenizer.texts_to_sequences(chats)
    input_to_predict = pad_sequences(sequences, maxlen=max_len)
    input_to_predict = np.array(input_to_predict)
    input_to_predict = np.array(input_to_predict)
    positiveScore = 0
    negativeScore = 0
    output = model.predict(input_to_predict)
    # print("output: ", output)
    for i in output:
        if(i[0] > 0.5):
            positiveScore = positiveScore+1
        else:
            negativeScore = negativeScore+1
    # laplacian correction
    if(positiveScore <= 0):
        positiveScore = 1
    if(negativeScore <= 0):
        negativeScore = 1
    totalScore = positiveScore/(positiveScore+negativeScore)
    totalScore = round(totalScore, 2)
    return (totalScore, positiveScore, negativeScore)


# print(predict(chats=["Yes Yes Yes Yes YES!!!", "I am so so happy",
#       "Today is the best day", "This is just great"]))

# print(predict(chats=['I am so sad', "All the misfortunes are given to me", "This was a very bad day"
#       "I was in an accident and now I have to pay for my car's reapirs. I am already short on money and I am not sure if I will even be able to pay rent next week"]))
