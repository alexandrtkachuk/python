#zmq серевер который принимает url и вернет html , будет пока работать с tor

from pyvirtualdisplay import Display
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.proxy import *
import zmq
import time
import sys


def loadSite(url):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    #profile.set_preference("network.proxy.http", "92.241.226.174")
    #profile.set_preference("network.proxy.http_port", 16632)
    profile.set_preference("network.proxy.socks", "localhost")
    profile.set_preference("network.proxy.socks_port", 9050)
    profile.update_preferences()
    #
    display = Display(visible=0, size=(800, 600))
    display.start()
    path_to_chromedriver = '/home/alexandr/python/prs/files/geckodriver'
    browser = webdriver.Firefox(firefox_profile = profile, executable_path = path_to_chromedriver)
    #
    browser.delete_all_cookies()
    browser.get(url)
    #print(browser.page_source)
    #print(browser.page_source)
    html =  browser.page_source
    #
    browser.close()
    display.stop()
    #
    return html

#loadSite('http://myip.ru/')
context = zmq.Context()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)
    if(message == b'done'):
        print("good")
        break;
    #  Do some 'work'
    time.sleep(1)
    try:
        html = loadSite( message.decode())
        #  Send reply back to client
    except Exception as ex:
        socket.send(b'none')
        print('Some Exeption:', ex)
    else:
        socket.send(html.encode())


print("good\n")

