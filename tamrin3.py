import re

# logs
log1 = '2024/07/11 15:30:45 [error] 1234#1234: *56789 connect() failed (111: Connection refused) while connecting to upstream, client: 192.168.1.100, server: example.com, request: “GET /api/data HTTP/1.1”, upstream: “http://127.0.0.1:8000/api/data”, host: “example.com”, referrer: “https://example.com/”'
log2 = '2024/07/11 16:15:20 [error] 1234#1234: *67890 open() “/usr/share/nginx/html/not_found.html” failed (2: No such file or directory), client: 192.168.1.101, server: example.com, request: “GET /nonexistent-page HTTP/1.1”, host: “example.com”, referrer: “https://example.com/”'

# regex pattern for parsing logs
log_pattern = re.compile(
    r'(?P<datetime>\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] '
    r'(?P<process_id>\d+#\d+): \*(?P<connection_id>\d+) (?P<message>.*?) '
    r'client: (?P<client_ip>[\d.]+), server: (?P<server>[^,]+), request: “(?P<request>[^”]+)”, '
    r'(upstream: “(?P<upstream>[^”]+)”, )?host: “(?P<host>[^”]+)”, referrer: “(?P<referrer>[^”]+)”'
)

# function definition for parsing logs
def parse_log(log):
    match = log_pattern.match(log)
    if match:
        return match.groupdict()
    return None

#parsing logs
parsed_log1 = parse_log(log1)
parsed_log2 = parse_log(log2)

# test
print("Parsed Log 1:", parsed_log1)
print("Parsed Log 2:", parsed_log2)
