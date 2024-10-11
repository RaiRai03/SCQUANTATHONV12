import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, mean_absolute_error
from keras.models import Sequential
from keras.layers import Input, Dense

# Define a function to extract features from QRNG data
def extract_features(qrng_data):
    features = []
    for data in qrng_data:
        # Check if data is not empty
        if len(data) > 0:
            # Check if data is numerical
            data_num = pd.to_numeric(data, errors='coerce')
            if not np.isnan(data_num).any():
                try:
                    # Calculate statistical properties (e.g., mean, variance, entropy)
                    mean = np.mean(data_num)
                    var = np.var(data_num)
                    # Add a small value to avoid division by zero
                    epsilon = 1e-10
                    data_num_smoothed = data_num + epsilon
                    entropy = np.sum(-data_num_smoothed * np.log2(data_num_smoothed))
                    features.append([mean, var, entropy])
                except Exception as e:
                    print(f"Error calculating features: {e}")
                    print(f"Skipping data: {data}")
            else:
                print(f"Skipping non-numerical or invalid data: {data}")
        else:
            print(f"Skipping empty data: {data}")
    return np.array(features)

# Load dataset
df = pd.read_csv('datascript.csv')

# Print column names
print(df.columns)

# Print the first few rows of the dataset
print(df.head())
# Check if any column contains Python code
for column in df.columns:
    if 'import' in str(df[column].values):
        print(f"Column '{column}' contains Python code. Dropping it.")
        df = df.drop(column, axis=1)
    elif df[column].dtype == 'object':
        print(f"Column '{column}' is of type object. Dropping it.")
        df = df.drop(column, axis=1)

# Check if 'label' column exists
if 'label' not in df.columns:
    # Create a label column (replace with a more meaningful value if needed)
    df['label'] = 0

# Extract features from QRNG data
X = extract_features(df.drop('label', axis=1).values)
y = df['label']