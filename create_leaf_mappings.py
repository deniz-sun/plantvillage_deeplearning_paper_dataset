import os
import pandas as pd
import csv  # Import the csv module for additional settings

folder_name = "Grape___healthy"
base_directory = "raw/color/" + folder_name
base_csv_dir = "leaf_grouping/corrected_leafmaps/" + folder_name + ".csv"


data = []
leaf_number = 1
for filename in os.listdir(base_directory):
    parts = filename.split("___")
    if len(parts) > 1:
        filename = parts[1]
        temp_leaf_number = str(leaf_number) + '.0'
        row = [filename, temp_leaf_number]
        print(row)
        data.append(row)
        leaf_number += 1

df = pd.DataFrame(data, columns=['File Name', 'Leaf #'])
df.to_csv(base_csv_dir, index=False, quoting=csv.QUOTE_ALL)
print(f"CSV created for folder: {folder_name}")