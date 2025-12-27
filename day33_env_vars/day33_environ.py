import os
import json
from pathlib import Path

user=os.environ.get("USERNAME")
print("Current user:",user)

env=os.environ.get("APP_ENV","development")
print("Environment",env)

with open("config.json") as f:
    config=json.load(f)

base_dir=Path(os.environ.get("BASE_DIR","."))
input_dir=base_dir/config["input_dir"]

print("Input directory:",input_dir)
