from flask import Flask, jsonify, request, render_template
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os

app = Flask(__name__)

# Load model and tokenizer
MODEL_PATH = 'next_word_model.keras'
TOKENIZER_PATH = 'tokenizer.pkl'
CONFIG_PATH = 'model_config.pkl'

model = load_model(MODEL_PATH)
with open(TOKENIZER_PATH, 'rb') as f:
    tokenizer = pickle.load(f)

with open(CONFIG_PATH, 'rb') as f:
    config = pickle.load(f)

max_sequence_len = config['max_sequence_len']
vocab_size = config['vocab_size']

def predict_next_words(text, top_k=3):
    """Predict top k next words given text input"""
    try:
        seq = tokenizer.texts_to_sequences([text.lower()])[0]
        
        if not seq:
            return []
        
        # Pad the sequence
        seq = pad_sequences([seq], maxlen=max_sequence_len - 1, padding='pre')
        
        # Get predictions
        pred = model.predict(seq, verbose=0)[0]
        
        # Get top k indices
        top_indices = np.argsort(pred)[::-1][:top_k]
        
        results = []
        for idx in top_indices:
            word = tokenizer.index_word.get(idx, '<unknown>')
            confidence = float(pred[idx])
            
            # Skip unknown tokens
            if word not in ['<unknown>', '<OOV>']:
                results.append({
                    'word': word,
                    'confidence': round(confidence * 100, 1)
                })
        
        return results
    except Exception as e:
        print(f"Error in prediction: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'predictions': []})
    
    predictions = predict_next_words(text, top_k=3)
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
