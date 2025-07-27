import requests
from urllib.parse import urljoin

def test_xss(forms):
    xss_payload = "<script>alert('x')</script>"
    found = []

    for page_url, form in forms:
        action = form.get("action")
        method = form.get("method", "get").lower()
        inputs = form.find_all("input")

        data = {inp.get("name"): xss_payload for inp in inputs if inp.get("name")}
        target = urljoin(page_url, action)

        try:
            res = requests.post(target, data=data) if method == "post" else requests.get(target, params=data)
            if xss_payload in res.text:
                found.append({"url": target, "payload": xss_payload})
        except:
            continue

    return found
