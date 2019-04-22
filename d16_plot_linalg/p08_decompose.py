
"""
x+y = 5
2x + 4y = 18

x + y =5
2x + 4(5-x) = 18
2x + 20-4x =18
-x = -2

x + y =5
x =1

1 1
1 0

0 1 4
1 0 1

矩阵分解：
    |- 分解乘三角矩阵 -》 在分解成对角矩阵

QR分解好处：
    |- 把任何矩阵分解成：    T为转置矩阵
            |- 行列不相关就叫正交矩阵
            |- 正交矩阵Q  Q*Q*T=I   R ： 三角阵

奇异值分解：
    |- 任何一个矩阵M能分解为U E V     M=U E V     U阵（酉阵）
        |- 对角阵
"""
import numpy as np
import numpy.linalg as la

m = np.array([
    [1, 2, 3],
    [4, 9, 1],
    [7, 2, 6]
])
# r = la.qr(m)
#
# Q = r[0]
# R = r[1]
#
# print('Q:\n', Q)
# print('R:\n', R)
# print(np.matmul(Q, Q.T))    #  单位矩阵


# r = la.svd(m)       # 奇异值分解
# print(r[0])
# print(r[1])
# print(r[2])
# print(np.matmul(r[0], r[0].T))

print(la.norm(m, 1, axis=0))        # 矩阵范数
print(la.cond(m, 2))        # m与逆矩阵的条件数

"""
向量与范数：
0-范数： 矩阵中非0元素的个数
1-范数： 矩阵中绝对值的和
2-范数： 所有元素的平方和开发

numpy矩阵的范数：
0范数： 没有定义
1范数： 列向量的最大值
2范数： M.MT的最大特征值的平方根
"""
print(la.det(m))        # m的行列式
print(la.matrix_rank(m))    # 矩阵的志


