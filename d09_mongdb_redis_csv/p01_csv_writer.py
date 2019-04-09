import csv
import codecs

# 准备好已经打开的文件
fd = open('tencent.csv', 'w')
# 数据格式（数据字段）准备写入的字段
fields = ['课程名称', '机构名称', '报名人数', '课程价格', '学习方式']

writer = csv.DictWriter(f=fd, fieldnames=fields, dialect='excel')   # 打开的文件 写入的字段 打开的方言（格式）
# 编码（DOM）
        #  加上这一句要出错 注释掉
# fd.write(codecs.BOM_UTF8.decode('utf-8'))   # BOM_UTF8，用每个文件前面三个字节用来表达

# 写一个头
writer.writeheader()

# 写多个行 数据是一个字典
# data = {}                       #  第一种写法
# data['课程名称'] = 'Python开发'
# data['机构名称'] = '马哥'
# data['报名人数'] = '100'
# data['课程价格'] = '7288.00'
# data['学习方式'] = '随到随学'
# writer.writerow(data)

                                #  第二种写法
data2 = {
    '课程名称':'K8S精通',
    '机构名称':'马哥',
    '报名人数':'88',
    '课程价格':'2000',
    '学习方式':'线上'
}
writer.writerow(data2)


fd.close()  # 关闭文件



















