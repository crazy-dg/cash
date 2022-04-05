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
    browser.get("https://cashmining.me/")
except:
    time.sleep(5)
time.sleep(5)

rw = RandomWords()
username = "laws"
browser.find_element_by_xpath("//a[@data-target='#login_box']").click()
time.sleep(1)
browser.find_element_by_xpath("//input[@placeholder='Username / Email']").send_keys(username)
browser.find_element_by_xpath("//input[@name='password']").send_keys('userpassword')
browser.find_element_by_xpath("//button[@name='connect']").click()

print(username)

count = 0
while (browser.current_url != "https://cashmining.me/index.php"):
    time.sleep(2)
    count += 1
    print("waiting...")
    if (count > 5):
        print("can't login")
        exit(-1)

browser.find_element_by_xpath(
    "//button[@class='btn btn-danger btn-sm w-100']").click()

print(browser.find_element_by_xpath("//b[@id='c_coins']").text)


print("start mining")

count = 0
while (count < 300):
    time.sleep(69)
    browser.refresh()
    time.sleep(1)
    try: 
        print(browser.find_element_by_xpath("//b[@id='c_coins']").text)
    except:
        print("can't get your balance")
        exit(-1)
    count += 1
