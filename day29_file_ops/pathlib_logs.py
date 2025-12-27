from pathlib import Path
from datetime import datetime

base_dir=Path(".")
logs_dir=base_dir/"logs"
log_file=logs_dir/"actions.log"

logs_dir.mkdir(exist_ok=True)

timestamp=datetime.now().strftime("%Y-%m=%d %H:%M:%S")

with log_file.open("a") as f:
    f.write(f"{timestamp}-Moved .txt files from input to processes\n")
