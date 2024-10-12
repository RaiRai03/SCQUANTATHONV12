import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data(data):
    # Perform exploratory data analysis (EDA)
    print(data.describe())

    # Visualize the data
    sns.pairplot(data)
    plt.show()