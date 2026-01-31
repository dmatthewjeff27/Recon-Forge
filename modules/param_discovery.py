from urllib.parse import urlparse, parse_qs

class ParameterDiscovery:
    def extract(self, urls):
        params = {}
        for url in urls:
            parsed = urlparse(url)
            q = parse_qs(parsed.query)
            if q:
                params[url] = list(q.keys())
        return params
