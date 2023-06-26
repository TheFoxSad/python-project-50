import json
import re


def generate_gendiff(file1_path, file2_path):
    with open(file1_path) as file1, open(file2_path) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
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
    dict = json.dumps(result, indent=2)
    diff = re.sub(r'[",]', '', dict)
    return diff
