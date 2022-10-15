import json


def save(filename, obj):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False)


def load(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        return json.load(f)
