import json

# 定义json String

data = {
    'name': "kitty",
    'color': "pink"
}

print("before:", data)
print("before_type:", type(data))
# before_type: <class 'dict'>


json_dumps = json.dumps(data)
print('after:', json_dumps)
print("after_type:", type(json_dumps))
# after_type: <class 'str'>

# 转换:
myData = '{"name":"张三", "age":18}'
json_loads = json.loads(myData)
print(json_loads)  # {'name': '张三', 'age': 18}
print("after_type:", type(json_loads))
