from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
def search():
    driver.get('https://www.google.com')
    time.sleep(3)
    var1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
    time.sleep(1)
    var1.send_keys('Youtube')
    time.sleep(1)
    var2 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/span[1]/center/div[1]/img')
    time.sleep(1)
    var2.click()
    time.sleep(2)
    var3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]')
    time.sleep(1)
    var3.click()
    time.sleep(60)
search()