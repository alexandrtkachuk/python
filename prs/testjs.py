import os
from pyvirtualdisplay import Display
from selenium import webdriver
from pprint import pprint

display = Display(visible=0, size=(800, 600))
display.start()

path_to_chromedriver = '/home/alexandr/www/html/python/prs/files/geckodriver'
os.environ["webdriver.firefox.driver"] = path_to_chromedriver
browser = webdriver.Firefox(executable_path = path_to_chromedriver)
#browser = webdriver.Firefox()
browser.get('http://myip.ru/')

print(browser.page_source)

display.stop()
