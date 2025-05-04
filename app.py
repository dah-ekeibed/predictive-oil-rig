from flask import Flask, request, jsonify
from sklearn.linear_model import LogisticRegression
import joblib
import json
from simulated_blockchain import Blockchain  # Import blockchain class

app = Flask(__name__)

# Load the trained model
model = joblib.load('predictive_model.pkl')

# Initialize Blockchain
blockchain = Blockchain()

@app.route('/sensor-data', methods=['POST'])
def handle_sensor_data():
    try:
        # Get sensor data from the POST request
        data = request.get_json()

        # Extract values from the data
        corrosion_level = float(data['corrosion_level'])
        pressure = float(data['pressure'])
        temperature = float(data['temperature'])

        # Predict if maintenance is needed
        prediction = model.predict([[corrosion_level, pressure, temperature]])

        # Maintenance is needed if prediction is 1, otherwise not (0)
        maintenance_required = bool(prediction[0])  # Convert prediction to bool

        # Add the new data to the blockchain
        blockchain.add_data(corrosion_level, temperature, pressure, maintenance_required)

        # Add a new block to the blockchain
        blockchain.create_new_block(proof=200)

        # Print the blockchain to see the updated data
        blockchain.print_blockchain()

        # Return a proper JSON response with maintenance status
        return jsonify({
            'message': 'Data received and processed successfully.',
            'maintenance_required': maintenance_required
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
