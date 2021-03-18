"""
    目标：将python中的字典转为json字符串
    操作：
        1.导包 import json
        2.调用dumps()方法 将字典转换为json字符串
    注意：
        json中，还有一个方法dump()写入json，勿要选错
"""


# 导包
import json

"""将字典转换为json字符串"""
# 定义字典
data = {"name": "赞多", "age": 22}
# 调用dumps进行转换json字符串
print("转换之前的数据类型：", type(data))
data2 = json.dumps(data)
print("转换之前的数据类型：", type(data2))

"""将字符串转为json"""
# 定义字符串
string = '{"name":"力丸", "age":24}'
# 注意错误写法，属性名必须使用双引号
# string = "{'name':'力丸', 'age':24}"
print("转换之前：", type(string))
# 转换
string1 = json.loads(string)
print("转换之后：", type(string1))

