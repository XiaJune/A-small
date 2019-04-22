import numpy.random as rd
import matplotlib.pyplot as plt

"""
#laplace拉普拉斯分布
scale 偏差 方差 偏移

"""
# x = rd.laplace(loc=100, scale=100, size=(10000,))  #laplace拉普拉斯分布
# x = rd.normal(loc=100, scale=100, size=(10000,))  #正态分布
# x = rd.normal(loc=0, scale=1, size=(100000,))  #标准正态分布
x = rd.standard_normal(size=(100000,))              #标准正态分布


figure = plt.figure(1, figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.hist(
    x=x,
    bins=1000,

)

plt.show()







