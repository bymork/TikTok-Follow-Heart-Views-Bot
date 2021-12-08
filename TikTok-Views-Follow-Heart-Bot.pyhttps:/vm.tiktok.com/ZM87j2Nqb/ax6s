from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
from time import sleep
import sys

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/your/path/for/chromedriver',chrome_options=chrome_options) #If you use Windows you must add .exe

i = 0

def loop1():
    global i
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        driver.refresh()
        i += 1
        total = i * 1000
        print("Views success delivered! Total", total,"views")
        sleep(55)
        loop1()
    except:
        print("An error occured. Now will retry again")
        driver.refresh()
        loop1()

def loop2():
    sleep(10)
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop2()
    try:
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/form/div/div/button").click()
        sleep(10)
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[1]/div/form/button").click()
        sleep(10)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text
        sleep(55)
        print(hearts," Success delivered!")
        sleep(100)
        driver.refresh()
        sleep(200)
        loop2()
    except:
        print("An error occured. Now will retry again")
        driver.refresh()
        sleep(355)
        loop2()

def loop3():
    pass

def loop4():
    sleep(20)
    wait_time = 660 #11 minutes
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click() #Followers
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop4()
    try:
        sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div/form/div/input").send_keys(vidUrl) #Write
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid\"]/div/div/div/form/div/div/button").click() #Search
        sleep(20)
        driver.find_element_by_xpath("//*[@id=\"c2VuZF9mb2xsb3dlcnNfdGlrdG9r\"]/div[1]/div/form/button").click() #AddFollowers
        sleep(wait_time/3)
        print("Success delivered")
        sleep(wait_time/3)
        driver.refresh()
        sleep(wait_time/3)
        loop4()
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("An error occurred. Now will retry again")
        driver.refresh()
        sleep(wait_time)
        loop4()

vidUrl = "https://www.tiktok.com/@social_degradation_crazy/video/6890937108874169601" #Change with one of your tiktok videos

system("clear") #If you have Windows you can use cls
tiktokbot = pyfiglet.figlet_format("NoNameoN", font="slant")
print(tiktokbot)
print("Author: https://github.com/NoNameoN-A")
print("")

"""
You can change auto value below
auto = 1 for auto views OK
auto = 2 for auto hearts OK
auto = 3 for auto views + hearts InWork...
auto = 4 for auto followers OK
"""
bot = 1 #Change this

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    pass
else:
    loop4()
    pass

