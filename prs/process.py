from threading import Thread
from time import sleep
from pyvirtualdisplay import Display
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.proxy import *

class MyThread(Thread):

        def __init__(self, proxy = '74.84.131.34', port = 80, url = 'http://myip.ru/'):
            Thread.__init__(self)
            self.proxy = proxy
            self.port = port
            self.url  = url

        def run(self):
            print("run\n")
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", self.proxy)
            profile.set_preference("network.proxy.http_port", int(self.port))
            profile.update_preferences()
            #
            display = Display(visible=0, size=(800, 600))
            display.start()
            path_to_chromedriver = '/home/alexandr/www/html/python/prs/files/geckodriver'
            browser = webdriver.Firefox(firefox_profile = profile, executable_path = path_to_chromedriver)
            #
            browser.delete_all_cookies()
            browser.get(self.url)
            #print(browser.page_source)
            #print(browser.page_source)
            tree = etree.HTML( browser.page_source)
            #
            browser.close()
            display.stop()
            #
            nodes = tree.xpath('//table[@class="network-info"]//tr/td')
            for node in nodes:
                print(node.text)

#
b = MyThread('54.245.201.80', 3128)
b.setDaemon(True)
b.start()
c = MyThread()
c.start()
c.join() # дождаться завершения потока в основном потоке
b.join()
print("finish")

