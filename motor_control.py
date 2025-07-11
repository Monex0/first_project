def control_motor(action):
    if action == "STOP":
        print("[Motor] Stopping the motor.")
    elif action == "FORWARD":
        print("[Motor] Moving forward.")
    elif action == "REVERSE":
        print("[Motor] Reversing.")
    else:
        print("[Motor] Unknown command.")