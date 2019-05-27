from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from pyvirtualdisplay import Display
import time, datetime, random
from telegram import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb
from telegram.ext import CallbackQueryHandler, Updater

display = Display(visible=0, size=(800, 800))
display.start()

firefox_binary = '/home/peppuz/projects/alarm/chromedriver'
driver = webdriver.Chrome(firefox_binary)
bot = telegram.Bot(token="469959402:AAGhtG3nHGTAX2JtsrFs4p_rUuK1l4RvmNA")

pref = ["https://www.youtube.com/watch?v=OCwm08sTA5U", "https://www.youtube.com/watch?v=OCwm08sTA5U"]


wake_up = [0,30]
awake, counter = False, 0 


def active_alarm():
    while !awake:
        now =  datetime.datetime.now()
        time.sleep(30)
        if wake_up[0] <= now.hour and wake_up[1] <= now.minute :
            send_check()
            print("MUSIC STREAMING")
            # PRODUCTION: driver.get(random.choice(pref))
            time.sleep(180)
            driver.close()


def send_check():
    rkb = ikm([ikb['Si', callback_data='si'],ikb['Ancora no', callack_data="No"]])
    bot.send_message(admin, "Ti sei alzato???", reply_markup=rkb)


def callbackHandler(b, u):
    query = u.callback_query
    if query.data == "Si":
        counter += 1 
        if 3 <= counter: 
            # if the counter checks of awakeness 
            awake = True 
            counter = 0 
            driver.close()
        # if the counter of check is lower then keep allarming


if __name__ == '__main__':
    up = Updater(token='469959402:AAGhtG3nHGTAX2JtsrFs4p_rUuK1l4RvmNA')
    d = up.dispatcher
    d.add_handler(CallbackQueryHandler(callbackHandler))
    up.start_polling()
    up.idle()
