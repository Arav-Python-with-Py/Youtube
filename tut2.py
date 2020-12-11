from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
def yt():
    driver.get('https://www.youtube.com')
    time.sleep(1)
    var1 = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
    time.sleep(1)
    var1.send_keys('Python')
    time.sleep(1)
    var2 = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
    var2.click()
    time.sleep(60)
    driver.close()
yt()    