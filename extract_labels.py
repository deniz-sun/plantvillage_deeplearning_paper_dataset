import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('leaf_mappings.txt')

labels = data['Leaf #'].unique()

train_labels, test_labels = train_test_split(labels, test_size=0.2, random_state=42)

train_data = data[data['Leaf #'].isin(train_labels)]
test_data = data[data['Leaf #'].isin(test_labels)]


def process_data(data):
    processed_lines = []
    for index, row in data.iterrows():
        leaf_value = str(row['Leaf #'])
        if '.' in leaf_value:
            leaf_value = leaf_value.split('.')[0]
        new_line = row['File Name'] + "," + leaf_value
        processed_lines.append(new_line)
    return processed_lines


train_data = process_data(train_data)
test_data = process_data(test_data)


def write_data(filename, data):
    with open(filename, 'w+') as file:
        prev_prefix = None
        for line in data:
            current_prefix = line.split()[0]
            if prev_prefix is not None and current_prefix != prev_prefix:
                file.write("\n")
            file.write(line + "\n")
            prev_prefix = current_prefix

write_data('train.txt', train_data)
write_data('test.txt', test_data)

print("The dataset was split into train.txt and test.txt")
