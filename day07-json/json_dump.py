import json

myData = {
    "name": "monkey",
    "xoxo": "ox"
}

# 调用写入方法
with open(
        "./data/data02.json",
        "w",
        encoding="utf-8"
)as f:
    "ensure_ascii: 不使用ascii码"
    json.dump(myData, f, ensure_ascii=False)
