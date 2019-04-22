from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

# chrome_options这个选项的作用决定了有界面还是无界面
driver = WebDriver(executable_path='chromedriver',chrome_options=None )

driver.get('https://www.baidu.com')













