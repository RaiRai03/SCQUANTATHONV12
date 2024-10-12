import pandas as pd
from sklearn.impute import SimpleImputer

def load_data(file_path):
    # Load the CSV dataset
    data = pd.read_csv(file_path)

    # Impute missing values with the mean
    imputer = SimpleImputer(strategy='mean')
    data[['feature1', 'feature2']] = imputer.fit_transform(data[['feature1', 'feature2']])

    return data