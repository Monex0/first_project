def read_sensor_data():
    # Simulated sensor reading
    import random
    distance = random.randint(10, 100)  # cm
    print("[Sensor] Distance measured.")
    return distance