import numpy as np

# ndarray最大的好处是一组类型相同的元素。 类型不同的元素就用：DataFrame
# m = np.array([
#     [
#         [1,2,3,4],
#         [3,4,5,6],
#         [5,6,7,8]
#     ],
#     [
#         [1,2,3,4],
#         [3,4,5,6],
#         [5,6,7,8]
#     ],
#     [
#         [1,2,3,4],
#         [3,4,5,6],
#         [5,6,7,8]
#     ]
# ])

# n = m.reshape((6, 2))       # reshape数组转换 为6*2
# print(n)

# n = m.resize((6, 7))          # 也是转换数组 但是数不够的就会补零
# print(n)
# print(m)

# print(m.transpose())        # 这是行列转换 行变为列  列变为行

# 矩阵转置
# print(m.shape)              # 数组格式  3*3*4 4维空间#
# print(m.transpose(2,0,1).shape) # 把坐标转换 维度发生变换 交换坐标轴

# print(m.swapaxes(0,2))      # 交换0和2维  其他维度不变 # 维度不能重复转换
# print(m.flatten())          # 直接转化为一维数组 # 返回的是拷贝
# print(m.ravel())            # 这个也是转换为一维 但这是共享空间，内存
#
# n = m.ravel()
# n[3] = 88               # 这里改变了n  也会发生变换因为是共享空间
# print(m)

m = np.array([[[3]]])
n = m.squeeze()         #np.nexaxis: 是压缩维度
print(n)















