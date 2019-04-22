import numbers
import fractions
a = 20 + 20j

print(isinstance(False, numbers.Complex))
# print(a//20)  #不能运算的


# 代数域 = （S是集合，O是运算） 一个集合与O运算称为代数结构
print(a.imag, a.real)   # 实部 虚部
print(a.conjugate())    #(1+2)变成（1-2）

b = 0.75        # 这是实数，其实python中没有引入有理数概念

r = fractions.Fraction('0.75')
print(r.numerator, r.denominator)   # 打印分子跟分母(3, 4),0.75就是4分之3

print(isinstance(b, numbers.Rational))  # 查看b是否是有理数（False）
print(isinstance(r, numbers.Rational))  # 查看r是否是有理数(True)


c = 20
print(c.numerator, c.denominator)   # 打印分子跟分母











