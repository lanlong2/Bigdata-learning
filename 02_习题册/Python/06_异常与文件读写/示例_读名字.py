from pathlib import Path

base = Path(__file__).resolve().parent
input_file = base / "练习数据" / "names.txt"
names = []

with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        name = line.strip().lower()
        if name:
            names.append(name)

print(names)
print(len(names))
