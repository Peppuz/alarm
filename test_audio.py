from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
import time, datetime, random

display = Display(visible=0, size=(800, 800))
display.start()
firefox_binary = '/home/peppuz/projects/alarm/chromedriver'
driver = webdriver.Chrome(firefox_binary)
pref = ["https://www.youtube.com/watch?v=OCwm08sTA5U", "https://www.youtube.com/watch?v=OCwm08sTA5U"]
driver.get(random.choice(pref))
time.sleep(1000)
driver.close()

