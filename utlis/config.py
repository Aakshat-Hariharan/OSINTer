import yaml, os

CONFIG_FILE = "config.yaml"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f) or {}
    return {}

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(data, f)
