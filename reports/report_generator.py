import json

def generate(report, output="reports/report.json"):
    with open(output, "w") as f:
        json.dump(report, f, indent=4)
