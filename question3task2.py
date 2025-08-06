import os

os.makedirs("data_output", exist_ok=True)

for file in os.listdir("data_input"):
    if file.endswith(".txt"):
        with open(f"data_input/{file}", "r") as f:
            lines = f.readlines()

        new_lines = []
        word_count = 0

        for line in lines:
            if not line.strip().startswith("#"):
                line = line.replace("temp", "permanent")
                word_count += len(line.split())
                new_lines.append(line)

        with open(f"data_output/{file}", "w") as f:
            f.writelines(new_lines)

        print(f"{file}: {len(new_lines)} lines, {word_count} words")

"""
OUTPUT:
Naresh@DESKTOP-MGP9AJ0 MINGW64 ~/OneDrive/PYTHONSCRIPT/PYTHON-PRACTICE (main)
$ python question3task2.py
example.txt: 1 lines, 6 words
"""
