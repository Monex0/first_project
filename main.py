from sensor_utils import read_sensor_data
from motor_control import control_motor
from algo_core import compute_path

def main():
    print("Starting robot system...")

    # Step 1: Get sensor data
    distance = read_sensor_data()
    print(f"Sensor distance: {distance} cm")

    # Step 2: Run algorithm logic
    decision = compute_path(distance)
    print(f"Decision: {decision}")

    # Step 3: Control motor based on decision
    control_motor(decision)

    print("Robot operation complete.")

main()