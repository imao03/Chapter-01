# 导包
import json

file = './data/login.json'
with open(
        file,
        "r",
        encoding="utf-8"
) as f:
    json_load = json.load(f)
    print(json_load)
