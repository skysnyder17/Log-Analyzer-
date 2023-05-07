import heapq

def aggregate_logs(log_files, output_file):
    log_iterators = []

    for log_file in log_files:
        file_iterator = open(log_file, 'r')
        log_iterators.append((file_iterator, next(file_iterator, None)))

    with open(output_file, 'w') as output:
        for timestamp, log in heapq.merge(*log_iterators):
            output.write(log)

    for file_iterator, _ in log_iterators:
        file_iterator.close()

# Usage
log_files = ['log1.txt', 'log2.txt', 'log3.txt']
output_file = 'aggregated_logs.txt'
aggregate_logs(log_files, output_file)
