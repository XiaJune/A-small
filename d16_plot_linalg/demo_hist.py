import matplotlib.pyplot as plt
import csv

# 1. 读取数据；数据数组
data = []
headers = ['工作年限' ,'学历','职位','薪水','城市','发布时间']
city = set()
with open('jobs.csv', 'r', encoding='utf-8') as fd:
    reader = csv.DictReader(fd, fieldnames=headers) # 返回的是迭代器
    next(reader)    # 把头略过
    for row in reader:
        data.append(row['城市'])
        city.add(row['城市'])
# print(data)
# print(city, len(city))
# 2. 显示数据matplotlib
figure = plt.figure('职位数量分布图', figsize=(8, 6))

ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-1, 12)
ax.hist(
    x=data,
    bins=len(city),
    range=(0, 12),       # 0到12 全部统计
    rwidth=0.6,            # 控制柱状图的大小宽度
    align='left',
    density=True,
    color='blue',
    # orientation='vertical'      # 默认就是这个

)

plt.show()
















































