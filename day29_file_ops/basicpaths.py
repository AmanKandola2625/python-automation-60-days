import os

print(os.getcwd())
print(os.path.exists("log.txt"))

os.makedirs("output",exist_ok=True)
print("Folder ready.")

for name in os.listdir("."):
    print(name)


if os.path.exists("log.txt"):
    os.rename("log.txt","output/log.txt")
    print("Moved log.txt to output/")
