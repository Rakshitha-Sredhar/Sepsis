import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

def preprocess_all_csvs(folder_path, selected_columns):
    all_data = []

    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            df = pd.read_csv(os.path.join(folder_path, file))

            # Select relevant columns and fill missing values
            df = df[selected_columns]
            df = df.ffill().bfill().dropna()  # <- updated here (no FutureWarning)

            all_data.append(df)

    # Combine all data from all files
    full_data = pd.concat(all_data)

    # Normalize the features
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(full_data)

    return scaled_data, scaler
