import requests

class TechDetector:
    def detect(self, host):
        tech = {}
        try:
            r = requests.get(f"http://{host}", timeout=5)
            tech["server"] = r.headers.get("Server")
            tech["x_powered_by"] = r.headers.get("X-Powered-By")
        except:
            pass
        return tech
