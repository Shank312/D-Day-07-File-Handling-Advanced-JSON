JSON Config Loader

This project demonstrates advanced file handling in Python using the built-in json module.
It loads application settings from a JSON configuration file (config.json) and applies them in program logic.


📂 Project Structure
Day 07/
│── File Handling Advanced + JSON/
│   ├── json_config_loader.py   # Python script to load & use JSON config
│   ├── config.json             # Configuration file (settings in JSON)


⚙️ Features

Reads configuration from an external JSON file.

Converts JSON data into a Python dictionary.

Accesses and prints individual configuration values.

Uses a setting (theme) in program logic.

Demonstrates safe file handling with with open(...).


📝 Example config.json

{
    "app_name": "SuperApp",
    "version": "1.0",
    "author": "John",
    "theme": "dark",
    "refresh_interval": 60
}


🐍 Example Code (json_config_loader.py)

import json

# Step 1: Open and read config.json
with open("config.json", "r") as file:
    config = json.load(file)                # Load JSON into Python dictionary

# Step 2: Access values
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


▶️ How to Run

Save both files (config.json and json_config_loader.py) in the same folder.

Open a terminal / command prompt inside that folder.

Run the script using Python:
python json_config_loader.py


✅ Example Output
Application Name:  SuperApp
Version:  1.0
Author:  John
Theme:  dark
Refresh Interval:  60 seconds
Dark mode enabled


💡 Use Cases

Store app settings like theme, refresh interval, or user preferences.

Store API keys or database credentials securely.

Load ML model parameters (batch size, learning rate) from config files.

Create portable and flexible programs where changing config.json updates behavior without modifying code.
