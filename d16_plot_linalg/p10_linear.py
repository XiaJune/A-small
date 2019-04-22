import matplotlib.pyplot as plt
import numpy as np
import sklearn.datasets as ds       # 数据集
import sklearn.linear_model as lm   # 线性

figure = plt.figure('线性回归', figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])

# 加载鸢尾花数据
data, target = ds.load_iris(return_X_y=True)
# data；样本sample
# target: 标签label

ax.scatter(
    data[0:150, 0],
    data[0:150, 2],
)
lr = lm.LinearRegression()
# 训练函数
lr.fit(
    X = data[50:150],
    y = target[0:100],
)
b = lr.intercept_       # 直线的截距
k = lr.coef_            # 斜率

# 计算样本
for d in data[50:100]:
    r = lr.predict([d])       # 小于0.5 属于target等于0的分类
    if r[0] <= 0.5:
        print('数据A')
    else:
        print('数据B')

for d in data[100:150]:
    r = lr.predict([d])       # 小于0.5 属于target等于0的分类
    if r[0] <= 0.5:
        print('数据A')
    else:
        print('数据B')


plt.show()







