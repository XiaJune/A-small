"""
    功能： 组合百度翻译的UI与百度翻译爬虫模块， 形成完整的翻译业务逻辑
    作者： Miller
    日期： 2019-04-10
"""
import baidu.baidudialog
import baidu.baiducrawler

class BaiduApp:
    def __init__(self):
        self.__crawler = baidu.baiducrawler.BaiduCrawler()
        self.__dlg = baidu.baidudialog.BaiduDialog(self.__crawler)

    def start(self):
        print('开始应用')
        self.__dlg.show()



