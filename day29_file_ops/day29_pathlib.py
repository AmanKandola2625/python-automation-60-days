from pathlib import Path

p=Path("output")

p.mkdir(exist_ok=True)

for f in p.iterdir():
    print(f.name)
