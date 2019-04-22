import numpy as np
"""
内积

matmul 矩阵乘法
dot     向量乘法
"""
# x = [1, 2, 3, 4, 5]
# y = [3, 4, 5, 6, 7]
#
# # 内积：dot, inner, matmul
# print(np.dot(x, y))         # 是一维就是向量处理 二维就是矩阵处理
# print(np.inner(x, y))       # 内积 向量
# print(np.matmul(x, y))      # 矩阵积

x = np.array([[1, 2, 3, 4, 5]])
y = np.array([[3, 4, 5, 6, 7]])

print(np.dot(x, y.T))
print(np.inner(x, y))
print(np.matmul(x, y.T))

