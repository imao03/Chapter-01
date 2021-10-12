import json

# 读Json ---> load

fd_file = "./data/writJson.json"

with open(
        fd_file,
        "r",
        encoding="utf-8"
) as f:
    load = json.load(f)

print(load)
