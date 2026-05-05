import random
import time

def read_sensor_data():
    temperature = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    distance = round(random.uniform(5.0, 100.0), 2)

    return {
        "temperature": temperature,
        "humidity": humidity,
        "distance": distance
    }

while True:
    data = read_sensor_data()

    print("Sensor Data:")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Humidity: {data['humidity']} %")
    print(f"Distance: {data['distance']} cm")

    if data["distance"] < 20:
        print("Warning: Collision risk detected!")
    else:
        print("Status: Safe")

    print("-" * 30)
    time.sleep(2)
