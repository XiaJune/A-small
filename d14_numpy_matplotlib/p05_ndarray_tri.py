import numpy as np

# m1 = np.diag([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ], k=-1)
# print(m1)   #  对角数

m2 = np.tri(4,4, k=-2, dtype=np.float32)
print(m2)

m3 = np.mat([1, 2, 3])      # 函数创建矩阵
print(m3)
