import math

"""
累加和累乘 还有累除最容易产生无穷大
"""
f1 = float('NaN')   # 有限数
f2 = float('Inf')   # 无穷数
print(math.isinf(f2))       # 是否是无穷数
print(math.isnan(f1))       #是否是数字
print(math.isfinite(20))    # 是否是有限数

print(math.exp(10))         # 自然指数
print(math.log(10,10))      # 对数（1.0）


print(math.hypot(1, -1))

print(math.sinh(1))
print((math.exp(1) - math.exp(-1))/2)

print(math.erf(1))  # 误差函数：就算正态分布原函数
print(math.erfc(1)) # 反误差函数
print(1-math.erfc(1))   # 1减去反误差等于误差



