from pathlib import Path
from datetime import datetime
import shutil
import json

#load config

with open("config.json","r") as f:
    config=json.load(f)

input_dir=Path(config["input_dir"])
backups_dir=Path(config["backups_dir"])
zips_dir=Path(config["zips_dir"])
logs_dir=Path(config["logs_dir"])
log_file=logs_dir/"actions.log"

#Ensure folders exist
backups_dir.mkdir(exist_ok=True)
logs_dir.mkdir(exist_ok=True)
zips_dir.mkdir(exist_ok=True)

#create timestamp backup
timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder=backups_dir/f"backup_{timestamp}"
shutil.copytree(input_dir,backup_folder)

#optional ZIP
if config["enable_zip"]:
    shutil.make_archive(str(zips_dir/backup_folder.name),"zip",backup_folder)

#Log action
log_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with log_file.open("a") as f:
    f.write(f"{log_time}-Backup created using config: {backup_folder}\n")

    print("Backup completed using configuration")
