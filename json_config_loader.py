
import json

# Step 1: Open and read config.json
with open("config.json", "r") as file:
    config = json.load(file)                # Load JSON into Python dictionary

# Step 2: Acces values
print("Application Name: ", config["app_name"])
print("Version: ", config["version"])
print("Author: ", config["author"])
print("Theme: ", config["theme"])
print("Refresh Interval: ", config["refresh_interval"], "seconds")


# Step 3: Use the config in the program logic
if config["theme"] == "dark":
    print("Dark mode enabled")
else:
    print("Light mode enabled")
