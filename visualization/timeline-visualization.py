import pandas as pd
import matplotlib.pyplot as plt

def visualize_log_timeline(log_file):
    df = pd.read_csv(log_file, parse_dates=['timestamp'], infer_datetime_format=True)
    df['event_count'] = 1
    df = df.set_index('timestamp')

    events_per_day = df.resample('D').sum()

    plt.figure(figsize=(12, 6))
    events_per_day['event_count'].plot(kind='line')
    plt.title('Log Event Timeline')
    plt.xlabel('Date')
    plt.ylabel('Number of Events')
    plt.show()

# Usage
log_file = 'log_data.csv'
visualize_log_timeline(log_file)
