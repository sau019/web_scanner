import requests
from urllib.parse import urljoin

def test_access_control(base_url):
    paths = ["/admin", "/dashboard", "/config", "/settings"]
    accessible = []

    for path in paths:
        full_url = urljoin(base_url, path)
        try:
            res = requests.get(full_url)
            if res.status_code == 200 and "login" not in res.text.lower():
                accessible.append(full_url)
        except:
            continue

    return accessible
