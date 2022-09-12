from selenium import webdriver
from time import sleep
import random


url = 'https://my.ntu.edu.tw/mattend/ssi.aspx'
driver = webdriver.Chrome()
driver.get(url)


# 設定隨機延時
def slp():
    sleep(random.randint(2, 5))


# 點擊登入
driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/div/div/p[1]/a').click()
slp()

account = 'user_name'
password = 'user_pw'

# 網頁登錄
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[1]/input').send_keys(account)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[3]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/button[1]').click()
slp()

# 點擊簽到
driver.find_element_by_id('btSign').click()
slp()

driver.quit()
