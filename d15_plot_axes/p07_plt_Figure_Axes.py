import matplotlib.pyplot as plt

figure = plt.figure(
    num='坐标演示图像',
    figsize=(8,6),
    dpi=100,
    facecolor='gray',
)
# a = figure.subplots(2,2)      # 很难控制 一般不使用
# print(a)
# ax = figure.gca()
# print(ax)

# ax = figure.get_axes()
# ax = figure.add_subplot(222, facecolor='red', label='A', title='Aa', position=[0.5, 0.5, 0.3, 0.3])
# ax = figure.add_subplot(221, facecolor='green', label='B', title='Bb')
# ax = figure.add_subplot(224)

ax = plt.Axes(
    figure,
    rect=[0.1, 0.1, 0.8 ,0.8]
)
figure.add_axes(ax)

# -------------
ax.set_position([0.2, 0.2, 0.6, 0.6])
ax.set_xlabel(
    xlabel='x坐标',
    fontdict={
        'fontsize':8,
        'fontweight':'bold',
        'fontstyle':'italic',
        'verticalalignment':'baseline',
        'horizontalalignment':'center',
        'color':'yellow'
    }
)

ax.set_ylabel(
    ylabel='y坐标',
    fontdict={
        'fontsize':8,
        'fontweight':'bold',
        'fontstyle':'italic',
        'verticalalignment':'baseline',
        'horizontalalignment':'center',
        'color':'yellow'
    }
)

ax.set_xbound(lower=0, upper=100)
ax.set_ybound(lower=-100, upper=100)

ax.set_xlim(left=0, right=10)

# ax.set_xscale('linear')                 # 控制刻度
ax.set_xticks(
    ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],   # 自己写的刻度
    minor=True                                  # 父刻度
)

ax.set_xticklabels(
    labels=['A','B','C','D','E','F','G','H','I','J'],
    fontdict={
        'fontsize':8,
        'fontweight':'bold',
        'fontstyle':'italic',
        'verticalalignment':'baseline',
        'horizontalalignment':'center',
        'color':'red'
    },
    minor=True)
# -------------
ax.plot(
    x=[0, 1, 2, 3,  6, 7, 8, 9, 10],
    y=[0.5, 0, 1, 1, 0, 1, 0, 1, 0,],
    linewidth=4,
    linestyle='--',
    marker='o',             # 折线起点形装
    markerfacecolor='red',
    markersize=15,
    color=(1,1,0,1),         # 线条的颜色
    markeredgewidth=2,
    markerfacecoloralt=(1,0,1,1)
)

# ax.plot(
#     x=[0, 1, 2, 3,  6, 7, 8, 9, 10],
#     y=[0.5, 0, 1, 1, 0, 1, 0, 1, 0,],
#     ''
# )
# # -------------


ax.legend()
# figure.legend()             # 绘制主题：图中存在Artist的时候才会绘制
figure.show()
figure.savefig('a.png')

plt.show()






























