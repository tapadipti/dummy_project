import os, json, random, yaml

params = yaml.safe_load(open("params.yaml"))["train"]
accuracy = params["accuracy"]


metrics_dict = {"loss": 0.1, "accuracy": random.random()}
METRICS_FILE = os.path.join("metrics.json")
with open(METRICS_FILE, "w") as f:
    f.write(json.dumps(metrics_dict))
