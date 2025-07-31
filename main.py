from platform_detect import detect_device 
import platform
from loading_json import *
import ui_dekstop, ui_linux




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