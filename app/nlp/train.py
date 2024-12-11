import tensorflow as tf
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import numpy as np

# Load intents
with open('app/nlp/intents.json', 'r') as f:
    intents = json.load(f)

# Prepare data
patterns = [intent['patterns'][0] for intent in intents['intents']]
responses = list(range(len(intents['intents'])))
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns).toarray()
y = tf.keras.utils.to_categorical(responses, num_classes=len(intents['intents']))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(intents['intents']), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=100, batch_size=8)
model.save('chat_model.h5')
