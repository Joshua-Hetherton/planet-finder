import platform

def detect_device():
    try:
        device=platform.machine().startswith("arm")
        if device:
            return "linux"
        else:
            return "windows"
    except Exception as e:
        print(f"Error detecting device: {e}")
        return "unknown"
    