import numpy as np

# 构造一个指定形状与类型的数组(空的数组的数据是随机：没有初始化的数据)
# na = np.ndarray(shape=(3,3), dtype=np.int8)
# print(na)


# 使用缓存构造有数据的数组
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
buffer = bytes(lst)

# na = np.ndarray(
#     shape=(3, 3),        # 这是构建3*3的数组
#     dtype=np.int8,
#     buffer=buffer,
#     offset=0,
#     strides=(2, 2))     # 行从哪里开始间隔多少字节 列每一列间隔多少字节

na = np.ndarray(
    shape=(3, 3),        # 这是构建3*3的数组
    dtype=np.int8,
    buffer=buffer,
    offset=0,
    # order='C'           # 行优先填充
    order = 'F'         # 列优先填充
)
print(na)















