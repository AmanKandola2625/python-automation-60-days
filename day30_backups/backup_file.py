from pathlib import Path
from datetime import datetime
import shutil

base=Path(".")

input_dir=base/"input"
backups_dir=base/"backups"
logs_dir=base/"logs"
log_file=logs_dir/"actions.log"

backups_dir.mkdir(exist_ok=True)
logs_dir.mkdir(exist_ok=True)

timestamp=datetime.now().strftime("%Y-%m-%d_%H%M%S")
backup_folder=backups_dir/f"backup_{timestamp}"

shutil.copytree(input_dir,backup_folder/"input")

log_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with log_file.open("a") as f:
    f.write(f"{log_time}-Backup created at {backup_folder}\n")

    print("backup completed successfully")
