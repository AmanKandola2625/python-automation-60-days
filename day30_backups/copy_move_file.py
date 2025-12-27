import shutil

shutil.copy("input/sample.txt","processed/sample.txt")

shutil.copytree("input","backup_input",dirs_exist_ok=True)

shutil.move("input/sample.txt","processes/sample.txt")
