"""
二维的直方图

# 颜色映射：
Axes.hist2D()


cmap参数： 颜色映射
"""
import matplotlib.pyplot as plt
import numpy.random as rd
import matplotlib.cm as clm

x = rd.randn(10000)
y = rd.randn(10000)

figure = plt.figure('2D直方图', figsize=(8, 6))   # 空间大小 800*600
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.hist2d(
    x=x,
    y=y,
    bins=100,
    range=[[-5, 5],[-5, 5]],
    cmap=clm.get_cmap('Paired')
)


plt.show()





