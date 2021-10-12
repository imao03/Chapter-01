"""
    目标：读取
    方法：load
"""
# 导包 json
import json

# 获取文件流 并调用 load方法
with open("./data/login.json",
          "r",
          encoding="utf-8"
          ) as f:
    data = json.load(f)
print(data)
