import json
import re
from .parser import parse_file


def generate_gendiff(file1_path, file2_path):
    data1 = parse_file(file1_path)
    data2 = parse_file(file2_path)
    result = {}
    all_keys = set(list(data1.keys()) + list(data2.keys()))
    for key in sorted(all_keys):
        if key not in data1:
            result[f'+ {key}'] = data2[key]
        elif key not in data2:
            result[f'- {key}'] = data1[key]
        elif data1[key] != data2[key]:
            result[f'- {key}'] = data1[key]
            result[f'+ {key}'] = data2[key]
        else:
            result[f'  {key}'] = data1[key]
    diff = json.dumps(result, indent=2)
    diff = re.sub(r'[",]', '', diff)
    return diff
