import requests
import bs4
'''
pip install lxml # lxml parser - needs to be installed but not imported ---only if using lxml as parser rather than html.parser

https://stackoverflow.com/questions/46490626/getting-all-links-from-a-page-beautiful-soup

'''
url = 'http://www.acontecaeventos.com.br/marketing-promocional-sao-paulo'
r = requests.get(url)
html_content = r.text
soup = bs4.BeautifulSoup(html_content, 'html.parser')  # or 'lxml'
links = soup.find_all('a')

for link in links:
    print(type(link)) # returns <class 'bs4.element.Tag'>
    print(link)
    print(link['href'])
    #print(link.get('href')) #same