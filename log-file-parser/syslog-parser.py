import re

def parse_syslog(log_file):
    pattern = r'(\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2}) (\S+) (\S+): (.*)'

    with open(log_file, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                timestamp = match.group(1)
                hostname = match.group(2)
                log_level = match.group(3)
                message = match.group(4)
                # Process or store the extracted information as needed
                print(f"Timestamp: {timestamp}, Hostname: {hostname}, Log Level: {log_level}, Message: {message}")

# Usage
log_file = 'syslog.log'
parse_syslog(log_file)
