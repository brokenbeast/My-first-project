from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://tieba.baidu.com/")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='com_userbar']/ul/li[4]/div/a").click()
time.sleep(1)
driver.find_element_by_class_name("tang-pass-footerBarULogin").click()
time.sleep(1)
driver.find_element_by_class_name("pass-text-input-userName").send_keys('18514040124')
time.sleep(1)
driver.find_element_by_class_name("pass-text-input-password").send_keys("jaz7413")
time.sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
time.sleep(1)
c = driver.get_cookies()
print(c)
time.sleep(5)
a = driver.find_element_by_xpath('//*[@id="likeforumwraper"]/a[1]').get_attribute('href')

b = driver.find_elements_by_xpath('//a[@class="u-f-item unsign"]')
print(a)
for x in b:
    x.click()
    time.sleep(2)

time.sleep(3)

# headers = {'Accept': '*/*',
#                'Accept-Language': 'en-US,en;q=0.8',
#                'Cache-Control': 'max-age=0',
#                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
#                'Connection': 'keep-alive',
#                'Referer': 'http://www.baidu.com/'
#                }
# f=open(r'test.txt','r')#打开所保存的cookies内容文件
# cookies={}#初始化cookies字典变量
# for line in c.split(';'):   #按照字符：进行划分读取
#     #其设置为1就会把字符串拆分成2份
#     name,value=line.strip().split('=',1)
#     cookies[name]=value
# cookies = str(int(c))
# url = 'http://tieba.baidu.com'
# r = requests.get(url,cookies = cookies)
# print(r)
driver.close()
# total_url = []
# for eve_url in url_chi:
#     eve_tieba_url = "http://tieba.baidu.com" +eve_url.text
#     total_url.append(eve_tieba_url)
# for eve_tieba in total_url:
#     driver.get(eve_tieba)
#     time.sleep(3)
#     driver.find_element_by_class_name('j_signbtn sign_btn_bright j_cansign').click()
#     try:
#         driver.find_element_by_class_name('j_signbtn sign_btn_bright j_cansign').click()
#     except:
#         pass
#     time.sleep(3)
