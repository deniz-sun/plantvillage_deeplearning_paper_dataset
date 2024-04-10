def format_txt(path):
    with open(path, 'r') as file:
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
            print(newLine)
        else:
            i += 1
    with open(path, "w") as file2:
        for line in processed_lines:
            file2.write(line + "\n")
    file.close()
    file2.close()

train_path = "hdf5/color-80-20/train.txt"
test_path = "hdf5/color-80-20/test.txt"
format_txt(train_path)
format_txt(test_path)