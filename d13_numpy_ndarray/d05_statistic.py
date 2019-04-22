from statistics import *

lst = [1, 2, 3, 4, 5, 6, 7]
# print(mean(lst))            # 算出平均数
# print(harmonic_mean(lst))   # 调和平均数
# print(median(lst))          # 中间那个数
# print(median_low(lst))      # 如果个数是偶数就是中间小的那个
# print(median_high(lst))     # 如果个数是偶数就是中间大的那个
# print(median_grouped(lst))  # 分组连续数值的中值，取插值
#

print(pstdev(lst))              # 偏差  偏差等于方差求平方根得到
print(pvariance(lst))           # 有偏方差（总体方差）  方差等于（x-平均数）**2  这个求平均数是除以数据长度
print(stdev(lst))               # 偏差
print(variance(lst))            # 无偏方差（样本方差）  方差等于（x-平均数）**2  这个求平均数是除以数据长度-1

print(pvariance(lst, mu=5))        # 指定方差计算的平均数




















