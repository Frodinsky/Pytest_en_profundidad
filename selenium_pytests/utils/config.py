import yaml
import os

def load_config():
    with open("../config.yaml", "r") as file:
        return yaml.safe_load(file)