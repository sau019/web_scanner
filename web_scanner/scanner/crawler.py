import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from bs4.element import Tag

def crawl(url):
    visited = set()
    forms = []
    urls_to_visit = [url]

    while urls_to_visit:
        current_url = urls_to_visit.pop()
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            res = requests.get(current_url, timeout=5)
            soup = BeautifulSoup(res.text, "lxml")

            # ✅ Extract forms
            for form in soup.find_all("form"):
                if isinstance(form, Tag):
                    forms.append((current_url, form))

            # ✅ Extract internal links
            for link in soup.find_all("a", href=True):
                if isinstance(link, Tag):
                    href = link.get("href")
                    if isinstance(href, str):  # Ensure href is a string
                        full_url = urljoin(current_url, href)
                        if urlparse(full_url).netloc == urlparse(url).netloc:
                            urls_to_visit.append(full_url)

        except Exception as e:
            print(f"[!] Error crawling {current_url}: {e}")
            continue

    return visited, forms
