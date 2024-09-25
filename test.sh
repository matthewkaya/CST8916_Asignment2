#!/bin/bash

# Base URL for API
BASE_URL="http://127.0.0.1:5000"

# Test: Get average temperature
echo "Testing GET /average-temperature..."
curl -X GET "${BASE_URL}/average-temperature"
echo -e "\n"

# Test: Add new sensor data (POST)
echo "Testing POST /sensor-data..."
curl -X POST "${BASE_URL}/sensor-data" \
    -H "Content-Type: application/json" \
    -d '{"timestamp": "2023-05-28T10:50:00", "temperature": 28.0, "humidity": 65.0, "pressure": 1015.0}'
echo -e "\n"

# Test: Update sensor data (PUT)
echo "Testing PUT /sensor-data/2023-05-28T10:50:00..."
curl -X PUT "${BASE_URL}/sensor-data/2023-05-28T10:50:00" \
    -H "Content-Type: application/json" \
    -d '{"timestamp": "2023-05-28T10:50:00", "temperature": 29.0, "humidity": 63.0, "pressure": 1014.0}'
echo -e "\n"

# Test: Partially update sensor data (PATCH)
echo "Testing PATCH /sensor-data/2023-05-28T10:50:00..."
curl -X PATCH "${BASE_URL}/sensor-data/2023-05-28T10:50:00" \
    -H "Content-Type: application/json" \
    -d '{"temperature": 30.0}'
echo -e "\n"

# Test: Delete sensor data (DELETE)
echo "Testing DELETE /sensor-data/2023-05-28T10:50:00..."
curl -X DELETE "${BASE_URL}/sensor-data/2023-05-28T10:50:00"
echo -e "\n"


# Test completed
echo "All tests completed."
