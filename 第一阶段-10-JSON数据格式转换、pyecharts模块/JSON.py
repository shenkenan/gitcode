import json

data = [{"name":"张大山", "age":11},{"name":"王大锤", "age":13},{"name":"张大山", "age":16}]
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

d = {"name":"周杰伦", "地址":"台湾"}
json_str1 = json.dumps(d, ensure_ascii=False)
print(json_str1)
print(type(json_str1))

s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "张大山", "age": 16}]'
l = json.loads(s)
print(l)
print(type(l))

s = '{"name": "周杰伦", "地址": "台湾"}'
d = json.loads(s)
print(d)
print(type(d))