from flask import Flask, render_template, request
from scanner.crawler import crawl
from scanner.vulnerabilities import xss, sqli
from scanner.access_control import test_access_control
from scanner.headers import test_headers

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        crawled_urls, forms = crawl(url)

        results = {
            "url": url,
            "xss": xss.test_xss(forms),
            "sqli": sqli.test_sqli(crawled_urls),
            "access": test_access_control(url),
            "headers": test_headers(url)
        }

        return render_template("index.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
