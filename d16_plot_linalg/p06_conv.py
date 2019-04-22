import numpy as np
"""
卷积  
计算格式：
    |- r[0] = x0y0
    |- r[1] = x0y1 + x1y0
    |- r[2] = x0y2 + x1y1 + x2y0    # x上升 y在下降

"""
x = [1, 2, 3, 4, 5, 6]
y = [6, 5, 4, 3, 2, 1]

print(np.convolve(x,y))









