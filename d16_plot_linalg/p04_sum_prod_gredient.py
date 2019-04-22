import numpy as np
"""
gradient(f, *varargs, **kwargs)
    |- 两边的梯度：左边是相邻两个相减得到 右边也是
    |- 中间的梯度值是两边元素相减然后跟中间数做
"""

a = [
    [1, 5, 6],
    [2, 6, 8],
    [6, 8, 10]
]

# print(np.sum(a))        # 数组里面所有的元素求和
# print(np.sum(a, axis=0))    # 按照行就和
# print(np.prod(a))       # 数组里面的元素相乘

# a = [
#     [1, 5, 6],
#     [2, np.NaN, 8],
#     [6, 8, 10]
# ]
# print(np.nansum(a, axis=0)) # 非数字 行求和

# print(np.diff(a))       # 差分 相邻两个元素相减
# print(np.gradient(a, axis=0))       # 按照行求梯度
# print(np.gradient(a, axis=1))       # 按照列计算梯度


b = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]
"""
cross:  
    索引列相加等一奇数就乘1 等于偶数就乘-1
"""
print(np.cross(a, b))       # 行差集

print(np.trapz([1, 2, 3]))  # 积分公式
















