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

while True:
    now =  datetime.datetime.now()
    time.sleep(30)
    if now.hour == 7 and now.minute == 30:
        # https://www.youtube.com/watch?v=OCwm08sTA5U -- Crimewave
        driver.get(random.choice(pref))
        time.sleep(200)
        driver.close()



"""
ideas: telegram bot che ogni 10 minuti o 5 minuti chiede se sei sceglio dalle 7:30 alle 11. alla ricezione di tre o due conferme laallarmw si blocca fino al giorno dopo 

impostare telegram con solo callback query handler e invio con messaggio pre inpostato 

"""
