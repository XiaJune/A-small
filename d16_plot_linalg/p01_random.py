import numpy as np
import numpy.random as rd

"""
# 随机小数
rand:[0, 1] 之间的随机数
randn:(-inf, inf)正无穷到负无穷之间的随机数，每个数字取到的概率满足正太分布（简称高斯分布） math.NaN, numpy.inf

#随机整数
randint
random_integers

# 也是取随机数    取的都是0到1之间随机数 备选【0-1】
random
ranf
sample

# 
choice(a[,replace, p])
"""

# print(rd.rand(3, 4))        #  这里打印的是0-1之间的3行4列数组
# print(rd.randn(3, 4))       # 正无穷到负无穷的3行4列数组

# print(rd.randint(1,5, dtype=np.int, size=(3, 4)))   # 1到5之间类型为int的3行四列数组
# print(rd.random_integers(1, 5, size=(3, 4)))        # 默认就是int类型 跟上面一样

# print(rd.random(size=(3, 4)))       #都是0到1之间
# print(rd.ranf(size=(3, 4)))
# print(rd.sample(size=(3, 4)))
# print(rd.random_sample(size=(3, 4)))

a = [1, 2, 3, 4, 5, 6]
m = rd.choice(a, size=(3, 4), replace=True)     # 指定可以重复选，若指定不重复选就必须让a中的值大于数组需要
print(m)

























