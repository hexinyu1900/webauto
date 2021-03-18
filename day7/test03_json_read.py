"""
    目标：读取json
    操作：
        1.导包json
        2.方法load
    注意：
        1.读取操作 r
        2.读取方法：load()而不是loads()
"""

# 导包
import json
# 打开要读取的文件流并调用load方法
with open("../data/write.json", encoding="utf-8") as f:
    data = json.load(f)
    print(data)