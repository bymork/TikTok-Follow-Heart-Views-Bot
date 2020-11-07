from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 650)

i = 0
a = 0
x = 0

def loop1():
    global i
    time.sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1()
    try:
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        driver.refresh()
        i += 1
        total = i * 1000
        print("Views success delivered! Total", total,"views")
        time.sleep(55)
        loop1()
    except:
        print("An error occured. Now will retry again")
        driver.refresh()
        loop1()

def loop2():
    pass

def loop3():
    pass

def loop4():
    pass

vidUrl = "YOUR_URL" #Change YOUR_URL to your Tik Tok video URL. This URL used to get views or hearts or both
#username = "YOUR_USERNAME" #Change YOUR_USERNAME to your Tik Tok username

system("cls")
tiktokbot = pyfiglet.figlet_format("NoNameoN", font="slant")
print(tiktokbot)
print("Author: https://github.com/NoNameoN-A")
print("")

"""
You can change auto value below
auto = 1 for auto views
auto = 2 for auto hearts InWork...
auto = 3 for auto views + hearts InWork...
auto = 4 for auto followers InWork...
"""
bot = 1 #Change this

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    pass
elif bot == 3:
    pass
else:
    pass