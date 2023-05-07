import heapq

def aggregate_logs(log_files, output_file):
    logs = []

    for log_file in log_files:
        with open(log_file, 'r') as file:
            for line in file:
                timestamp = extract_timestamp(line)  # Function to extract timestamp from the log line
                logs.append((timestamp, line))

    sorted_logs = heapq.nsmallest(len(logs), logs)

    with open(output_file, 'w') as output:
        for _, log in sorted_logs:
            output.write(log)

# Usage
log_files = ['log1.txt', 'log2.txt', 'log3.txt']
output_file = 'aggregated_logs.txt'
aggregate_logs(log_files, output_file)
