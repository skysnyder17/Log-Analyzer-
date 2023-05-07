def aggregate_logs(log_files, output_file):
    with open(output_file, 'w') as output:
        for log_file in log_files:
            with open(log_file, 'r') as file:
                for line in file:
                    output.write(line)

# Usage
log_files = ['log1.txt', 'log2.txt', 'log3.txt']
output_file = 'aggregated_logs.txt'
aggregate_logs(log_files, output_file)
