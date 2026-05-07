import yaml

def load_yaml(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)