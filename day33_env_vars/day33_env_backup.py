import os
import json
from pathlib import Path
from datetime import datetime

env=os.environ.get("APP_ENV","dev").lower()
print(f"Running in {env} mode")

#3) Map env to dev/prod naming
#If user sets APP_ENV=production, we treat it as prod

if env in ("prod","production"):
    env_tag="prod"
else:
    env_tag="dev"

#4) Build backup folder name backup_dev_YYYYMMDD or backup_prod_YYYYMMDD

date_str=datetime.now().strftime("%Y%m%d")
backup_folder_name=f"backup_{env_tag}_{date_str}"

print("Backup folder name:",backup_folder_name)

#5 log
logs_dir=Path("logs")
logs_dir.mkdir(exist_ok=True)
log_file=logs_dir/"actions.log"

timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with log_file.open("a") as f:
    f.write(f"{timestamp}-APP_ENV={env} ->mode={env_tag},backup_folder-{backup_folder_name}\n")

print("Logged to logs/actions.log")
