import requests

class SubdomainEnumerator:
    def __init__(self, domain):
        self.domain = domain

    def enumerate(self):
        url = "https://crt.sh/"
        params = {"q": f"%.{self.domain}", "output": "json"}
        results = set()

        try:
            r = requests.get(url, params=params, timeout=10)
            for entry in r.json():
                for sub in entry["name_value"].split("\n"):
                    sub = sub.strip().lstrip("*.").lower()
                    if sub.endswith(self.domain):
                        results.add(sub)
        except Exception:
            pass

        return sorted(results)
