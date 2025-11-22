import pandas as pd
import os

# 📁 Change this to your folder where .psv files are located
folder_path = 'data/raw_psv'
output_folder = 'data/converted_csvs'


# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# 🔁 Loop through each .psv file and convert
for file in os.listdir(folder_path):
    if file.endswith('.psv'):
        psv_file = os.path.join(folder_path, file)
        csv_file = os.path.join(output_folder, file.replace('.psv', '.csv'))

        # Read and convert
        df = pd.read_csv(psv_file, sep='|')
        df.to_csv(csv_file, index=False)

        print(f"Converted: {file} → {csv_file}")
