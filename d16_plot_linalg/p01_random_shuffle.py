import numpy.random as rd
import numpy as np

a = np.arange(0, 10, 1)     
print(a)
r = rd.shuffle(a)       # 打乱数据
print(r, a)

a = np.arange(0, 10, 1)
r = rd.permutation(a)       # 洗牌 也是打乱
print(r, a)
