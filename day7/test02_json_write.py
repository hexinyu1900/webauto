"""
    目标：写入json
    操作：
        1.导包json
        2.方法dump
    注意：
        1.写入操作 w
        2.写入方法：dump()而不是dumps()
"""

# 导包
import json
# 定义写的容
data = {"name": "古驰", "age": 18}
# 获取文件流并写入数据
with open("../data/write.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)