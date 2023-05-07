import re

def parse_custom_log(log_file):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (\S+): (.*)'

    with open(log_file, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                timestamp = match.group(1)
                username = match.group(2)
                message = match.group(3)
                # Process or store the extracted information as needed
                print(f"Timestamp: {timestamp}, Username: {username}, Message: {message}")

# Usage
log_file = 'custom.log'
parse_custom_log(log_file)
