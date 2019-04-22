import numpy as np


# ndarray最大的好处是一组类型相同的元素。 类型不同的元素就用：DataFrame
m = np.array([
    [1,2,3,4],
    [3,4,5,6],
    [5,6,7,8]
])

# print(m.item(11))   # 这是看作一维数组 直接打印对应索引
# print(m.item(1, 1)) # 这是取 在1位置的数组中的索引为1的数
#
# m.itemset(1, 88)    # 一维的 吧索引为1的改为88
# print(m)
#
# print(m.tolist())   # 把数组平铺下来打印
# print(m.tobytes())  # 转换为 字节数组
#
# print(m.astype(dtype=np.float))  # 把数组变为浮点

# m.tofile('a.txt', sep='|', format='%08d')

# def convert(data):
#     print(data)
#     return int(data)
# n = np.loadtxt(
#     'a.txt',
#     dtype=np.int32,
#     delimiter='|',
#     converters={1:convert},
#     usecols=4,                   # 指定读到的列
#
# )
# print(n)
# print(n.reshape((3, 4)))        # 读出来是一维数组了  可以转成自己想要的数组


m.fill(99)      # 数据填充 全部变成 99
print(m)




