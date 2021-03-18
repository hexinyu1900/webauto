# 导包
import json


def read_json(filename):
    filepath = "../data/" + filename
    # 调用load方法
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    datas = read_json("calc.json")
    print(datas)
    """
        期望的格式：[(1,2,3),(222,222,444)]
        问题：
            1.返回的格式为字典？
    """
    # 新建空列表
    arrs = []
    for data in datas.values():
        arrs.append((data['num1'], data['num2'], data['num3']))
    print(arrs)