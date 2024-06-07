import re
import json

def parse_value(value):
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        return value.strip('"')
    if value.startswith('{{') and value.endswith('}}'):
        return json.loads(value.replace('{', '[').replace('}', ']'))
    if value.startswith('{') and value.endswith('}'):
        return list(map(int, value.strip('{}').split(',')))
    try:
        return int(value)
    except ValueError:
        return value

def parse_entry(entry):
    entry = entry.strip()
    key = re.match(r'\[(\d+)\]', entry).group(1)
    value = re.search(r'\{(.*)\}', entry, re.DOTALL).group(1)
    value = re.findall(r'(\w+)\s*=\s*(.*?),\n', value, re.DOTALL)
    entry_dict = {k: parse_value(v) for k, v in value}
    return int(key), entry_dict

def convert_to_json(data):
    entries = re.findall(r'\[\d+\]\s*=\s*\{.*?\},', data, re.DOTALL)
    result = {}
    for entry in entries:
        key, value = parse_entry(entry)
        result[key] = value
    return json.dumps(result, ensure_ascii=False, indent=4)

# 将你的数据填充在这里
data = '''

'''

json_output = convert_to_json(data)

with open('Resources/AttributeData.json', 'w', encoding='utf-8') as f:
    f.write(json_output)