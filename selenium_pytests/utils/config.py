import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    config_path = os.path.abspath(config_path)
    with open(config_path, "r") as file:
        return yaml.safe_load(file)