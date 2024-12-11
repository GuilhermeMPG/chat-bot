import tensorflow as tf
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Load pre-trained model and data
model = tf.keras.models.load_model('app/nlp/chat_model.h5')
with open('app/nlp/intents.json', 'r') as f:
    intents = json.load(f)

vectorizer = CountVectorizer()
vectorizer.fit([intent['patterns'][0] for intent in intents['intents']])

def get_response(user_input):
    input_vector = vectorizer.transform([user_input]).toarray()
    predictions = model.predict(input_vector)
    intent_index = np.argmax(predictions)
    response = intents['intents'][intent_index]['responses'][0]
    return response
