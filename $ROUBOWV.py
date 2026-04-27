import random
from datetime import datetime

ips = ["192.168.1." + str(i) for i in range(1, 255)]
methods = ["GET", "POST", "PUT"]
urls = ["/home", "/login", "/products", "/cart"]
status = [200, 200, 200, 404, 500]

with open("access.log", "w") as f:
    for _ in range(100000):
        ip = random.choice(ips)
        time = datetime.now().strftime("%d/%b/%Y:%H:%M:%S")
        method = random.choice(methods)
        url = random.choice(urls)
        stat = random.choice(status)
        size = random.randint(200, 5000)

        log = f'{ip} - - [{time}] "{method} {url} HTTP/1.1" {stat} {size}\n'
        f.write(log)

