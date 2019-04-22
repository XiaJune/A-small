import numpy as np

# m = np.array([
#     [1,2,3,4],
#     [3,0,0,6],
#     [5,6,7,8]
# ])

# axis=0 是按照索引取行 如果是1就是按照列来取
# print(m.take([1,0,2,1], axis=1))

# print(m.take([[1], [1]]))

# print(m.repeat(2))  # 每个元素重复几次

# print(m.compress([True,False,True]))    # 把数组拉平 True就选 False就不选
#
# print(m.diagonal(-0))   # 取索引对应的行对角线的数

# print(m.nonzero())      # 返回一个行列

# out = np.empty_like(m, dtype=np.int32)      # 创建一个跟m一样大小的数组
# n = m.choose(np.array([11,22,33,44,55,66,77,88,99,100]), out=out)    # 把m数组里面的元素做索引在这里面找值替换
# print(n)
# print(out)

# m = np.array([1,2,5,6,9])
# print(m.searchsorted(7))        # 排序到已有序的数组中插入7 返回插入的索引位置

m = np.array([
    [9,2,3,4],
    [3,6,2,0],
    [5,2,7,1]
])

# print(m)
# print(m.sort())         # 默认按照每一行排序   # 没有返回 直接在原数组操作
# print(m.sort(axis=0))   # 这就是列排序
# print(m)

# print(m)
# print(m.argsort())          # 返回新的数组 不修改原数组
# print(m.argsort(axis=0))   # 返回的是原数组的下标
# print(m)

# m = np.array([1,5,7,2,4,9,6,8])
# n = m.partition(1)  # 在原基础上面排序  不返回 # 这里指定索引几就排序几个 剩下的不管（部分排序）
n = m.argpartition(1)  # 这是返回的下标（索引）
print(m)
print(n)










