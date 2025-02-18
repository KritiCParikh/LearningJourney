### Question:
Given a log file, each line begins with some IP address, find the most frequent IP address.

### Concept Name:
**Hashing (Using Dictionary to Count Occurrences)**

### Explanation:
You can use a dictionary to store the frequency of each IP address in the log file. Iterate through each line of the log, extract the IP address, and update its count in the dictionary. After processing all lines, the IP address with the highest count will be the most frequent.

### Python Solution:

```python
from collections import defaultdict

def most_frequent_ip(logs):
    ip_count = defaultdict(int)  # Dictionary to store the count of each IP address
    
    # Iterate through each log line and count the IP addresses
    for log in logs:
        ip = log.split()[0]  # Assume the IP is the first part of the log line
        ip_count[ip] += 1
    
    # Find the IP with the maximum count
    most_frequent_ip = max(ip_count, key=ip_count.get)
    
    return most_frequent_ip

# Example usage
logs = [
    "192.168.1.1 - - [12/Dec/2024:13:00:00 +0000] \"GET / HTTP/1.1\" 200 1024",
    "192.168.1.2 - - [12/Dec/2024:13:05:00 +0000] \"POST /login HTTP/1.1\" 200 512",
    "192.168.1.1 - - [12/Dec/2024:13:10:00 +0000] \"GET /home HTTP/1.1\" 200 1024",
    "192.168.1.3 - - [12/Dec/2024:13:15:00 +0000] \"GET /about HTTP/1.1\" 200 1024",
    "192.168.1.1 - - [12/Dec/2024:13:20:00 +0000] \"GET /contact HTTP/1.1\" 200 1024"
]

print(most_frequent_ip(logs))  # Output: 192.168.1.1

```
## **Explanation of the Output:**
- defaultdict(int) is used to create a dictionary where missing keys are initialized to 0. This is useful for counting occurrences without checking if the key already exists.
- log.split()[0] is used to extract the IP address from the log line. This assumes the log format is consistent and the IP address is the first item in the line.
- max(ip_count, key=ip_count.get) finds the key (IP address) in the dictionary with the highest count.

## **Example Log File Input:**
192.168.1.1 - - [12/Dec/2024:13:00:00 +0000] "GET / HTTP/1.1" 200 1024
192.168.1.2 - - [12/Dec/2024:13:05:00 +0000] "POST /login HTTP/1.1" 200 512
192.168.1.1 - - [12/Dec/2024:13:10:00 +0000] "GET /home HTTP/1.1" 200 1024
192.168.1.3 - - [12/Dec/2024:13:15:00 +0000] "GET /about HTTP/1.1" 200 1024
192.168.1.1 - - [12/Dec/2024:13:20:00 +0000] "GET /contact HTTP/1.1" 200 1024

## **Output:**
192.168.1.1
