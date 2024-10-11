import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, mean_absolute_error
from keras.models import Sequential
from keras.layers import Input, Dense
from sklearn.impute import SimpleImputer  # Add this line

# Define a function to extract features from QRNG data
def extract_features(qrng_data):
    features = []
    for data in qrng_data:
        # Calculate statistical properties (e.g., mean, variance, entropy)
        mean = np.mean(data)
        var = np.var(data)
        # Add a small value to avoid division by zero
        entropy = np.sum(-data * np.log2(data + 1e-10))
        features.append([mean, var, entropy])
    return np.array(features)

# Load dataset
df = pd.read_csv('datascript.csv')

# Print column names
print(df.columns)

# Check if 'target' column exists
if 'target' in df.columns:
    # Extract features from QRNG data
    X = extract_features(df.drop('target', axis=1).values)
    y = df['target']

    # Impute missing values with mean
    imputer = SimpleImputer(strategy='mean')
    X = imputer.fit_transform(X)

    # Check if the number of samples is sufficient
    if len(X) > 1:
        # Split data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.1, random_state=42)

        # Check if the target variable has more than one unique value
        if len(np.unique(y)) > 1:
            # Train SVC model
            svc_model = SVC(kernel='rbf', C=1)
            svc_model.fit(X_train, y_train)

            # Evaluate model on validation set
            y_pred = svc_model.predict(X_val)
            print('Validation Accuracy:', accuracy_score(y_val, y_pred))
            print('Classification Report:')
            print(classification_report(y_val, y_pred))
        else:
            print("Error: The target variable has only one unique value.")
    else:
        print("Error: Not enough samples to split into training and validation sets.")
else:
    print("Error: 'target' column not found in the DataFrame.")