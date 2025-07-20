from platform_detect import detect_device 
import platform
import json
import ui_dekstop, ui_linux

## JSON functions
def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return None
def save_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

##


def main():
    ## Detects the device type and updates the config.json file accordingly if it has changed.
    try:
        detect_mode = detect_device()
        config=load_json('config.json')
        if config.get("MODE") != detect_mode:
            print(f"Detected device mode: {detect_mode}")
            config["MODE"] = detect_mode
            save_json('config.json', config)

    except Exception as e:
        print(f"An error has occurred: {e}")


    match detect_mode:
        case "linux":
            print("Running on Linux arm architecture")
            # Add Linux-specific code here
        case "windows":
            print("Running on Windows")
            ui_dekstop.create_ui()


            
            # Add Windows-specific code here
        case "unknown":
            print("Unknown device type, running default configuration")
            # Handle unknown device type
        case _:
            print("Unsupported device type")

    


main()