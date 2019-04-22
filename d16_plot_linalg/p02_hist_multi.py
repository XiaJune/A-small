import numpy.random as rd
import matplotlib.pyplot as plt

# 每一列表示一个直方图
x = rd.randn(10000, 3) # 3个数据长度 3个数据样本,

figure = plt.figure('多数据直方图', figsize=(8, 6))

ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
r = ax.hist(
    x=x,
    bins=100,                   # 控制每个数组中有多少元素
    stacked=True,
    color=['r','g','b'],
    histtype='step',
)
print(r)

plt.show()





















