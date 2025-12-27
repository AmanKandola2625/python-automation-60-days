import os

os.makedirs("input",exist_ok=True)

os.makedirs("processed",exist_ok=True)

os.makedirs("logs",exist_ok=True)

for name in os.listdir("input"):
    if name.endswith(".txt"):
        print("Found File:",name)

        src=os.path.join("input",name)
        dest=os.path.join("processed",name)

        os.rename(src,dest)
        print(f"Moved {name} to processed/")
