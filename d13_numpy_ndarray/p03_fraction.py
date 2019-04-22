import fractions,numbers

# 分式运算
a = fractions.Fraction(0.75)    #构造有理数
b = fractions.Fraction(numerator=3, denominator=4)  #构造有理数
print(a.numerator, a.denominator)   # 分子分母
print(b)    #3/4
print(a+b)  # 3/2

print(fractions.gcd(12,8))  # 求最大公约数(4)
print(isinstance(a, numbers.Rational))  # 是否是有理数












