import numpy as np
import matplotlib.pyplot as plt

"""
正旋曲线 sin
"""
fig = plt.figure(1, figsize=(8, 6))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-2 * np.pi, 2 * np.pi)
# x = np.linspace(-2 * np.pi, 2 * np.pi, 10)
x = np.linspace(-5, 5, 100)
# y = np.sin(x)       # 数值运算时按位运算 element-wize
y = np.sinh(x)

ax.plot(x, y)

plt.show()

p = [0, 1, 2, 6, 10]
print(np.unwrap(p))























