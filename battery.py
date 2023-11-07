import json
# Function to update the battery status in "bat.txt"
def update_battery_status():
    status = {"percentage": 0}  # Initialize with a default value

    try:
        with open("bat.txt", "r") as f:
            status = json.load(f)
    except FileNotFoundError:
        pass  # If the file doesn't exist yet

    # Extract the percentage from the battery status
    battery_percentage = status.get("percentage", 0)

    if battery_percentage <= 10:
        with open("bat.txt", "w") as f:
            f.write("true\n")  # Add a newline character
        print("File updated")
    else:
        with open("bat.txt", "w") as f:
            f.write("false\n")  # Add a newline character
        print("File updated")

update_battery_status()

