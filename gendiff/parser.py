import json
import yaml
from pathlib import Path

def parse_file(file_path):
    file_path = Path(file_path)
    file_suffix = file_path.suffix

    if file_suffix == '.json':
        with open(file_path) as f:
            data = json.load(f)
        return data

    elif file_suffix in ['.yaml', '.yml']:
        with open(file_path) as f:
            data = yaml.safe_load(f)
        return data

    else:
        raise ValueError(f"Unsupported file format: {file_suffix}")
