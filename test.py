from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import base64
import random

browser = webdriver.Firefox()
url = "http://splix.io"

# log in
def gameStart(browser):

    # set options
    time.sleep(1)
    uglyMode = browser.find_element_by_id("uglyText")
    if "on" not in uglyMode.text:
        uglyMode.click()

    time.sleep(1)
    quality = browser.find_element_by_id("qualityText")
    while "low" not in quality.text:
        quality.click()
        quality = browser.find_element_by_id("qualityText")

    # choose a name
    time.sleep(1)
    playerName = browser.find_element_by_id("nameInput")
    myname = "potato"
    while len(myname) > 0:
        playerName.send_keys(myname[0])
        time.sleep(random.randint(1,4)/8)
        myname = myname[1:]

    time.sleep(1)
    submitButton = browser.find_element_by_id("joinButton")
    submitButton.click()

# screen grab
def screenGrab(browser):
    canvas = browser.find_element_by_id("mainCanvas")
    sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
    canvas_base64 = browser.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)
    canvas_png = base64.b64decode(canvas_base64)
    with open(r"canvas"+sttime+".png", 'wb') as f:
        f.write(canvas_png)

# moves
def up(game):
    game.send_keys(Keys.ARROW_UP)

def down(game):
    game.send_keys(Keys.ARROW_DOWN)

def left(game):
    game.send_keys(Keys.ARROW_LEFT)

def right(game):
    game.send_keys(Keys.ARROW_RIGHT)


# strategy
def playGame(browser):
    game=browser.find_element_by_tag_name('body')
    time.sleep(0.2)
    up(game)
    right(game)
    time.sleep(0.2)
    while True:
        for n in range(30):
            up(game)
            time.sleep(0.4)
            right(game)
            time.sleep(0.4)
            down(game)
            time.sleep(0.5)
            left(game)
            time.sleep(0.4)
        for n in range(30):
            up(game)
            time.sleep(0.4)
            right(game)
            time.sleep(0.4)
            down(game)
            time.sleep(0.4)
            left(game)
            time.sleep(0.5)
        for n in range(30):
            up(game)
            time.sleep(0.5)
            right(game)
            time.sleep(0.4)
            down(game)
            time.sleep(0.4)
            left(game)
            time.sleep(0.4)
        for n in range(30):
            up(game)
            time.sleep(0.4)
            right(game)
            time.sleep(0.5)
            down(game)
            time.sleep(0.4)
            left(game)
            time.sleep(0.4)

# main
browser.get(url)
gameStart(browser)
playGame(browser)





#driver.close()
