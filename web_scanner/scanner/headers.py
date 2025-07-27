import requests

def test_headers(url):
    try:
        res = requests.get(url)
        headers = res.headers
        issues = []

        required = {
            "X-Frame-Options": "Clickjacking protection",
            "X-Content-Type-Options": "Prevent MIME type sniffing",
            "Content-Security-Policy": "Prevent XSS",
            "Strict-Transport-Security": "Force HTTPS",
            "Referrer-Policy": "Control referrer info"
        }

        for header, description in required.items():
            if header not in headers:
                issues.append(f"{header} missing - {description}")

        return issues
    except:
        return ["Header check failed."]
