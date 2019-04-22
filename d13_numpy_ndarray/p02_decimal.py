import decimal,numbers
"""
decimal： 定点和浮点运算
    |- 实现了精度更高的算法
    |- 想实现高精度的算法请不要使用int，float，请使用Decimal高精度类型
    |- 这是真牛逼(Decimal)
    
e = float('12.44444444444444444423234234232352352')
print(e)        # float是无法表示这么高的精度的(12.444444444444445)这么多位
"""

                    # 设置一个精度    设置四舍五入                 最大指数   最小只是
ctx = decimal.Context(prec=4, rounding=decimal.ROUND_CEILING, Emax=100, Emin=-100, capitals=1, clamp=True)
a = decimal.Decimal('12.44444444444444444423234234232352352')
# print(a)
b = decimal.Decimal('33.143141434124342342342342342342323323')
print(a+b)
print(isinstance(b, numbers.Number))    # True

# ctx = decimal.getcontext()
# print(ctx.prec)     # 夹紧
# print(ctx.rounding)
# print(ctx.flags)    # 每次运算产生的标记
# print(ctx.traps)    # 设置的标记
# print(ctx.Emin)     # 最小指数
# print(ctx.Emax)     # 最大指数
# print(ctx.clamp)    # 指数是否包含精度
# print(ctx.capitals) #  是否采用大小写 一般使用0和1表示科学计数法后面的e的大小写





