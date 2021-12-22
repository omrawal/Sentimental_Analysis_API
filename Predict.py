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
    model=keras.models.load_model(filepath='model.h5',compile = False)
    tokenizer.fit_on_texts(chats)
    sequences = tokenizer.texts_to_sequences(chats)
    input_to_predict = pad_sequences(sequences, maxlen=max_len)
    input_to_predict=np.array(input_to_predict)
    input_to_predict=np.array(input_to_predict)
    positiveScore=0
    negativeScore=0
    output=model.predict(input_to_predict)  
    for i in output:
        if(i[0]>0.5):
            positiveScore=positiveScore+1
        else:
            negativeScore=negativeScore+1
    totalScore=positiveScore/(positiveScore+negativeScore)
    return totalScore