import numpy as np

# Python的内置类型，python的类型缺陷：不存在大小写
# na = np.ndarray((3, 3), dtype=np.bool)

# Numpy的内置类型（直接使用numpy的内置类型）
# na = np.ndarray((3, 3), dtype=np.int128)  # 这是占128位

# numpy.dtype() 自己构造一个类型
# na = np.ndarray((3, 3), dtype=np.dtype(int))
# print(type(na.dtype))

dt = np.dtype('I')
na = np.ndarray((3, 3), dtype=dt)       # 这两个是一样的
# na = np.ndarray((3, 3), dtype='I')
print(na.dtype)

na = np.ndarray((3, 3), dtype='i4') # (2, 2)int 这两种一样
print(na.dtype)

na = np.ndarray((3, 3), dtype='U10')    # 这两个一样
na[1, 1] = 'Miller'
print(na)

na = np.ndarray((3, 3), dtype='U10,i4,f8')
na[1, 1][0] = 'Miller'
na[1,1][1]  = 20
na[1,1][2] = 88.88
print(na)

print('~~~~~~~~~~~~~~~~~~~')
na = np.ndarray(
    shape=(3, 3),
    dtype=np.dtype([('name',('U', 10)), ('age', 'i4')])
)
na[0, 0]['name'] = 'Miller'
na[0, 0]['age'] = 20
print(na)

na = np.ndarray(
    shape=(3, 3)
)
print(na)


