from flask import Flask, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the trained model
model_path = "../models/optimized_decision_tree.pkl"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"The model file was not found at {model_path}. Please check the path and try again.")

with open(model_path, "rb") as file:
    model = pickle.load(file)

# Root route
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'success',
        'message': 'Welcome to the Delivery Delay Prediction API! Use the /predict endpoint to make predictions.'
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features from request
        input_features = np.array([
            data['distance_km'],
            data['planned_delivery_days'], 
            data['actual_delivery_days'],
            data['weather_conditions'],
            data['traffic_conditions'],
            data['is_long_distance'],
            data['is_bad_weather'],
            data['is_heavy_traffic']
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_features)
        delay_prediction = "Delayed" if prediction[0] == 1 else "On Time"

        return jsonify({
            'status': 'success',
            'prediction': delay_prediction
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
