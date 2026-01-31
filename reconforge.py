import asyncio
from core.config_loader import load_config
from modules.subdomain_enum import SubdomainEnumerator
from modules.live_hosts import LiveHostDetector
from modules.port_scan import PortScanner
from modules.tech_detect import TechDetector
from modules.crawler import Crawler
from modules.param_discovery import ParameterDiscovery
from reports.report_generator import generate

def main(domain):
    config = load_config()
    report = {"domain": domain}

    subs = SubdomainEnumerator(domain).enumerate()
    report["subdomains"] = subs

    live = asyncio.run(LiveHostDetector().detect(subs))
    report["live_hosts"] = live

    ps = PortScanner()
    td = TechDetector()
    cr = Crawler()
    pd = ParameterDiscovery()

    report["hosts"] = {}

    for host in live:
        ports = ps.scan(host, config["ports"])
        tech = td.detect(host)
        urls = cr.crawl(f"http://{host}")
        params = pd.extract(urls)

        report["hosts"][host] = {
            "ports": ports,
            "tech": tech,
            "urls": urls,
            "params": params
        }

    generate(report)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
