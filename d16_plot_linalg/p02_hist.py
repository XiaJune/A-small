"""
直方图  数据统计
hist(
    x,                  # 显示的数据
    bins=None,          # 箱子的数量 好像是取一半
    range=None,         # 范围
    density=None,       # True显示密度，显示百分比（就是概念）  False就是统计次数
    weights=None,       # 统计次数的权重（出现1次记1.5次 不知道什么鬼）
    cumulative=False,   # 累加
    bottom=None, 
    histtype='bar',
    align='mid',
    orientation='vertical',
    rwidth=None, log=False,
    color=None, 
    label=None, 
    stacked=False,
     normed=None,           # 不推荐使用了 等价于density
    **kwargs)

"""
import numpy.random as rd
import matplotlib.pyplot as plt

# x = [1,2,3,1,3,4,1,3,2,4,5,2,1,5,6,5,3,2,1,1,4,5,6]
x = rd.randn(10000)


# 创建图
figure = plt.figure('随机频率直方图', figsize=(8, 6))
# 创建坐标系
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-5, 5)       # 只有最后一个包含6和7 其他都是前包后不包
# ax.set_ylim(0, 10)
# 画图
r = ax.hist(
    x=x,
    bins=100,
    range=[-5, 5],
    density=False,      # 默认是False 统计次数
    cumulative=False,  # 这是列加 False表示布雷加
    bottom=[0],           # 离底边的高 指定类型就需要是一个列表
    histtype='bar',     # step 梯状图
    align='mid',      # 图显示靠左边还是右边还是中间(mid)
    rwidth=0.5,         # 设置间隔
    color='b',          # 控制柱状图的颜色
    label='职位统计',       # 摘要显示 显示这个图是什么

)
# print(r)
ax.legend()
figure.show()
plt.show()




































