import pandas as pd
import matplotlib.pyplot as plt

def visualize_error_distribution(log_file):
    df = pd.read_csv(log_file)
    error_counts = df['error_type'].value_counts()

    plt.figure(figsize=(8, 8))
    error_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Error Distribution')
    plt.ylabel('')
    plt.show()

# Usage
log_file = 'log_data.csv'
visualize_error_distribution(log_file)
