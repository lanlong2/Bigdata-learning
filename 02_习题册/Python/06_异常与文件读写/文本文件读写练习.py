from pathlib import Path
base=Path(__file__).resolve().parent
input_dir=base/"我的输出"
input_dir.mkdir(exist_ok=True)
input_file=input_dir/"name_clean.txt"
names=["alice","bob","ailice"]
with open(input_file,"w",encoding="utf-8") as file:
    for name in names:
        file.write(name+"\n")

with open(input_file,"r",encoding="utf-8") as file:
    read_back=[line.rstrip("\r\n") for line in file]
print(read_back == names)
