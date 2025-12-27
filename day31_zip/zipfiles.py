import shutil
shutil.make_archive("my_backup","zip","input")

from datetime import datetime

timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
zip_name=f"backup_{timestamp}"

shutil.make_archive(zip_name,"zip","input")

shutil.make_archive("input_backup_zip","zip","backups")

shutil.unpack_archive("my_backup.zip","unzipped_folder")
