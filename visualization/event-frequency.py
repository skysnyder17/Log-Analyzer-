import pandas as pd
import matplotlib.pyplot as plt

def visualize_event_frequency(log_file):
    df = pd.read_csv(log_file)
    event_counts = df['event_type'].value_counts().nlargest(10)

    plt.figure(figsize=(12, 6))
    event_counts.plot(kind='bar')
    plt.title('Top 10 Log Event Frequency')
    plt.xlabel('Event Type')
    plt.ylabel('Frequency')
    plt.show()

# Usage
log_file = 'log_data.csv'
visualize_event_frequency(log_file)
