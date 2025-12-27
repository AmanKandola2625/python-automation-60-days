from pathlib import Path
from datetime import datetime
import shutil

base=Path(".")

backups_dir=base/"backups"
zips_dir=base/"zips"
logs_dir=base/"logs"
log_file=logs_dir/"actions.log"
#Ensure folder exist
zips_dir.mkdir(exist_ok=True)
logs_dir.mkdir(exist_ok=True)

#get latest backup folder

backup_folders=[f for f in backups_dir.iterdir() if f.is_dir()]

if not backup_folders:
    print("No backup folder found")
    exit()

latest_backup=max(backup_folders,key=lambda x: x.stat().st_mtime)

#create zip filename
zip_name=zips_dir/latest_backup.name

#create ZIP archive
shutil.make_archive(str(zip_name),"zip",latest_backup)

#log zip creation
timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with log_file.open("a") as f:
    f.write(f"{timestamp}-Zipped backup {latest_backup.name} to {zip_name}.zip\n")

print("ZIP archive created successfully")
