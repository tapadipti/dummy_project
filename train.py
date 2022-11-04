import os, json, random

metrics_dict = {"loss": random.random(), "accuracy": random.random()}
METRICS_FILE = os.path.join("metrics.json")
with open(METRICS_FILE, "w") as f:
    f.write(json.dumps(metrics_dict))
