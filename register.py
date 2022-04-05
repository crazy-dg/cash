from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import warnings
from random_words import RandomWords

warnings.filterwarnings('ignore')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches",['enable-automation','enable-logging'])
chrome_options.add_argument('log-level=3')
chrome_options.add_argument('disable-infobars')
chrome_options.add_extension(r'ublock.crx') 
browser = webdriver.Chrome(chrome_options=chrome_options)

try:
    browser.get("https://cashmining.me/?page=register")
except:
    time.sleep(5)
time.sleep(5)

rw = RandomWords()
username = rw.random_word()
browser.find_element_by_xpath("//input[@placeHolder='John_Doe']").send_keys(username)
browser.find_element_by_xpath("//input[@id='email']").send_keys(username + '@snapmail.cc')
browser.find_element_by_xpath("//input[@id='repeat_email']").send_keys(username + '@snapmail.cc')
browser.find_element_by_xpath("//input[@id='password']").send_keys('userpassword')
browser.find_element_by_xpath("//input[@id='repeat_password']").send_keys('userpassword')
Select(browser.find_element_by_xpath(".//select[@name='gender']")).select_by_index(1)
Select(browser.find_element_by_xpath(".//select[@name='country']")).select_by_index(47)
browser.find_element_by_xpath("//button[@name='register']").click()

print(username)
