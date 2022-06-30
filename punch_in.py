from selenium import webdriver
from time import sleep
import random


url = 'https://my.ntu.edu.tw/attend/ssi.aspx'
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
driver.find_element_by_xpath('/html/body/center/div/div[4]/form/table/tbody/tr[1]/td/input').send_keys(account)
driver.find_element_by_xpath('/html/body/center/div/div[4]/form/table/tbody/tr[2]/td/input').send_keys(password)
driver.find_element_by_xpath('/html/body/center/div/div[4]/form/table/tbody/tr[3]/td[2]/input').click()
slp()

# 點擊簽到
driver.find_element_by_id('btSign').click()
slp()

driver.quit()
