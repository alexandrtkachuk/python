from pyvirtualdisplay import Display
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.proxy import *

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "74.84.131.34")
profile.set_preference("network.proxy.http_port", int('80'))
profile.update_preferences()



display = Display(visible=0, size=(800, 600))
display.start()
path_to_chromedriver = '/home/alexandr/www/html/python/prs/files/geckodriver'
browser = webdriver.Firefox(firefox_profile = profile, executable_path = path_to_chromedriver)


browser.delete_all_cookies()
browser.get('http://myip.ru/')
#print(browser.page_source)
#print(browser.page_source)
tree = etree.HTML( browser.page_source)

browser.close()
display.stop()

nodes = tree.xpath('//table[@class="network-info"]//tr/td')
for node in nodes:
    print(node.text)
