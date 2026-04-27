
import re
import csv

pattern = r'(\d+\.\d+\.\d+\.\d+).*\"(\w+) (.*?) HTTP.*\" (\d+) (\d+)'

with open("access.log", "r") as infile, open("access_parsed.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["ip", "method", "url", "status", "size"])

    for line in infile:
        match = re.search(pattern, line)
        if match:
            writer.writerow([
                match.group(1),
                match.group(2),
                match.group(3),
                match.group(4),
                match.group(5)
            ])
