import re

def parse_apache_log(log_file):
    pattern = r'(\S+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\d+) (\d+)'

    with open(log_file, 'r') as file:
        for line in file:
            match = re.match(pattern, line)
            if match:
                ip_address = match.group(1)
                date = match.group(4)
                request = match.group(5)
                status_code = match.group(6)
                bytes_sent = match.group(7)
                # Process or store the extracted information as needed
                print(f"IP: {ip_address}, Date: {date}, Request: {request}, Status Code: {status_code}, Bytes Sent: {bytes_sent}")

# Usage
log_file = 'access.log'
parse_apache_log(log_file)
