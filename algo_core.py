def compute_path(distance):
    print("[Algo] Evaluating path based on distance...")
    if distance < 20:
        return "REVERSE"
    elif distance < 50:
        return "STOP"
    else:
        return "FORWARD"