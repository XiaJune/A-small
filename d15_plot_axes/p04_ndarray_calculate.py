import numpy as np

m = np.array([
    [9,2,3,4],
    [3,6,2,9],
    [5,2,7,1]
])
# n = m.max()   # 按照所有行取最大值
# n = m.max(axis=0)   # 安装每一列取最大值
# n = m.max(axis=-1, keepdims=True)   # 取每一行的最大值
# print(n)

n = m.argmax()   # 取出平铺的最大值索引
print(n)
















