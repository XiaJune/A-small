import matplotlib as mlb
import matplotlib.pyplot as plt
import matplotlib.figure

# 应该有FigureManager（全局，在plt内部管理）


# 创建Figure图像（显示一个图像：当前图像，激活图像）
#       |- Figure创建（自己创建的Figure要设置管理器，因为自己创建的没有被管理）
#       |- plt的函数来创建
# figure = plt.Figure() # 这种创建方式可以使用，但是需要使用FigureManager纳入管理
"""
figure(
    num=None,   # 可以是整数，字符串 (建议使用字符串)
    figsize=None,  
    dpi=None, 
    facecolor=None,
    edgecolor=None,
    frameon=True,
    FigureClass=Figure,
    clear=False,
    **kwargs)
"""
figure = plt.figure(            # 使用函数创建的 会自动纳入管理
    num='my',             # 窗体的标题 名字
    figsize=(8,6),            # 表面了高度和宽度
    dpi=100,                   # 这是像素
    facecolor=('xkcd:sky blue'),  # RGBA（红绿蓝）都是浮点数   A是阿尔法通道 透明通道
    edgecolor='red',
    frameon=True                    # 边界 False就代表没有
)
figure.linewidth = 10
# 创建坐标系Axes：图中可以有多个坐标系（同时显示，需要指定位置大小）
#       |- Axis坐标轴（XAxis, YAxis）
#           |- 刻度, 标签，格式化器
# Figure.add_axes(axes对象| 参数)
# 使用函数构建Figure
ax = plt.Axes(
    figure,
    rect=[0.1, 0.5, 0.8, 0.3],
    label = '坐标系2',
    facecolor=(0, 0, 1, 1),
    frameon=True,
    xscale='log',       # log是对数坐标
    yscale='linear'
)
figure.add_axes(ax)

figure.add_axes(
    [0,1, 0.1, 0.8, 0.3],
    projection='polar',
    label='坐标系1',
    facecolor=(0, 1, 0, 1),
    frameon=True,
    sharex=ax,
    sharey=ax,
    xscale='linear',
    yscale='log',
)

# 绘制图形Artist（分成很多类型：线条，矩形，文本，图像）


# 显示Figure（一定要被FigureManager管理的Figure才能显示）

# 显示窗体
figure.show(warn=True)
plt.show()
