'''
pip install beautifulsoup4
'''
import bs4
import requests
import pprint

#res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
#print(res.raise_for_status())
#print(res.status_code)

#soup = bs4.BeautifulSoup(res.text, 'html.parser')   #html.parser is optional but without it bs4 throws a warning

'''
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). 
This usually isn't a problem, but if you run this code on another system, 
or in a different virtual environment, it may use a different parser and behave differently.
The code that caused this warning is on line 11 of the file c:\_Repositories\PythonTest\Projects\PythonStudy1\web_scraping.py. 
To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.
'''

#find css selecter - browser - right click the element - select element
#right click element - select copy css path ----Chrome
#elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
#print(elems[0].text.strip())

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #print(soup.encode_contents()) #get inner html
    elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    return elems[0].text.strip()

#amazon product page
price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print(price)