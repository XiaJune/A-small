import tushare as tu
import sklearn.datasets
import cv2

# 数据结构1 pandas.core.frame.DataFrame
result = tu.get_industry_classified()
print(type(result))
print(result)

# 数据结构2 numpy.ndarray
data, target = sklearn.datasets.load_iris(return_X_y=True)
print(type(data))

# 图像
img = cv2.imread('baidu.png')
print(type(img))

# 数据可视化： metplotlib: ndarray + DataFrame




