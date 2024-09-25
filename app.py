from flask import Flask, jsonify, request

app = Flask(__name__)

sensor_data = [
    {
        "timestamp": "2023-05-28T10:30:00",
        "temperature": 25.5,
        "humidity": 60.2,
        "pressure": 1012.3
    },
    {
        "timestamp": "2023-05-28T10:35:00",
        "temperature": 25.8,
        "humidity": 59.8,
        "pressure": 1012.7
    },
    {
        "timestamp": "2023-05-28T10:40:00",
        "temperature": 26.1,
        "humidity": 59.5,
        "pressure": 1012.9
    }
]

# Task 1: Retrieve average temperature
@app.route('/average-temperature', methods=['GET'])
def get_average_temperature():
    # TODO: Implement code to calculate the average temperature
    # and return it as a JSON response
    if sensor_data:
        total_temp = sum(entry['temperature'] for entry in sensor_data)
        average_temp = total_temp / len(sensor_data)
        return jsonify({"average_temperature": average_temp})
    return jsonify({"message": "No data available"}), 404

# Task 2: Add a new sensor data entry
@app.route('/sensor-data', methods=['POST'])
def add_sensor_data():
    # TODO: Implement code to add a new sensor data entry
    # based on the request body JSON
    new_entry = request.get_json()
    required_fields = ['timestamp', 'temperature', 'humidity', 'pressure']
    
    if all(field in new_entry for field in required_fields):
        sensor_data.append(new_entry)
        return jsonify({"message": "Data added successfully"}), 201
    return jsonify({"message": "Missing fields"}), 400

# Task 3: Update an existing sensor data entry by timestamp
@app.route('/sensor-data/<timestamp>', methods=['PUT'])
def update_sensor_data(timestamp):
    # TODO: Implement code to update an existing sensor data entry
    # based on the provided timestamp and request body JSON
    updated_data = request.get_json()
    
    for entry in sensor_data:
        if entry['timestamp'] == timestamp:
            entry.update(updated_data)
            return jsonify({"message": "Data updated successfully", "updated_data": entry})
    return jsonify({"message": "Data not found"}), 404

# Task 4: Partially update an existing sensor data entry by timestamp
@app.route('/sensor-data/<timestamp>', methods=['PATCH'])
def patch_sensor_data(timestamp):
    # This method allows partial updates to an existing sensor data entry
    patch_data = request.get_json()
    
    for entry in sensor_data:
        if entry['timestamp'] == timestamp:
            entry.update(patch_data)
            return jsonify({"message": "Data partially updated", "updated_data": entry})
    return jsonify({"message": "Data not found"}), 404

# Task 5: Delete an existing sensor data entry by timestamp
@app.route('/sensor-data/<timestamp>', methods=['DELETE'])
def delete_sensor_data(timestamp):
    # This method deletes a sensor data entry based on the provided timestamp
    for i, entry in enumerate(sensor_data):
        if entry['timestamp'] == timestamp:
            del sensor_data[i]
            return jsonify({"message": "Data deleted successfully"}), 200
    return jsonify({"message": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
