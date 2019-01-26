'''
pip install selenium

selenium-python.readthedocs.io

I also had to download the geckodriver.exe and add it's location to PATH ---
actually I just copied it to the root of the python install dir

https://github.com/mozilla/geckodriver/releases

https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

#Stuff I tried before finding solution for geckdriver.exe error
import os, sys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
pythonRoot = os.path.split(sys.executable)[0]
firefoxLib = 'Lib\\site-packages\\selenium\\webdriver\\firefox'
firefoxLib = os.path.join(pythonRoot, firefoxLib)
print(firefoxLib)

binary = FirefoxBinary(firefoxLib)
browser = webdriver.Firefox(firefox_binary=binary)
'''
from selenium import webdriver
############
#VARIABLES
############
browser = webdriver.Firefox()
url = 'https://automatetheboringstuff.com'
#chapter0 = '.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a:nth-child(1)'

############
#ACTIONS
############
browser.get(url)
'''
#get chapter 0 link by css selector
elem = browser.find_element_by_css_selector(chapter0)
#click on link
#elem.click()

#find elements
elems = browser.find_elements_by_css_selector('p')
#print(type(elems))

#search for substring ('Windows XP') within a paragraph
for e in elems:
    if 'Windows XP' in e.text: # this is better and more efficient
        print(e.text)
    if e.text.find('Windows XP') is not -1:  # note the 'is not -1' piece at the end!!!
        print('Got it')
'''
#find elements
elems2 = browser.find_elements_by_css_selector('a')
#print(type(elems))

#search for substring ('Windows XP') within a paragraph
for e in elems2:
    if 'Chapter 0' in e.text:
        print(e.text)
        print(e.get_attribute('innerHTML'))
        #e.click()
        break #otherwise loop will continue after page has changed which will throw an error 

#Print entire webpage
elem = browser.find_element_by_css_selector('html')
print(elem.text)
'''
#serach field
searchElem = browser.find_element_by_css_selector('.search-field')
#Type text
searchElem.send_keys('Zophie')
searchElem.submit()
browser.back()
browser.forward()
browser.quit()
'''






