import pandas as pd
with open("test.txt", 'r') as file:
    lines = file.readlines()

i = 1
processed_lines = []
for line in lines:
    if line.strip():
        commaPos = line.find(",")
        if commaPos != -1:
            newLine = line[:commaPos] + " " + str(i)
        else:
            newLine = line.strip() + " " + str(i)
        processed_lines.append(newLine)
    else:
        i += 1
with open("mod_test.txt", "w+") as file2:
    for line in processed_lines:
        file2.write(line + "\n")