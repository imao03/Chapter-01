import json

# 写Json ---> dump

myData = {
    "name": "kitty",
    "color": "pink"
}

fd_file = "./data/writJson.json"

with open(
        fd_file,
        "w",
        encoding="utf-8"
) as f:
    "ensure_ascii: 不使用ascii码"
    json.dump(myData, f, ensure_ascii=False)
