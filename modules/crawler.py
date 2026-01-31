import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Crawler:
    def crawl(self, base_url):
        urls = set()
        try:
            r = requests.get(base_url, timeout=5)
            soup = BeautifulSoup(r.text, "html.parser")
            for link in soup.find_all("a", href=True):
                urls.add(urljoin(base_url, link["href"]))
        except:
            pass
        return list(urls)
