import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
 
url = 'https://www.amazon.in/s?k=watches&crid=1W4ONWNX7XEZA&sprefix=watche%2Caps%2C247&ref=nb_sb_noss_2'

r = requests.get(url, headers=headers)

data = {'Title' : [], 'Price' : []}

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

spans = soup.select('span.a-size-base-plus.a-color-base.a-text-normal')
for span in spans:
    print(span.string)
    data['Title'].append(span.string)

prices = soup.select('span.a-price')
for price in prices: 
    if not('a-text-price' in price.get('class')):
        print(price.find('span').get_text())
        data['Price'].append(price.find('span').get_text())

df = pd.DataFrame.from_dict(data)
df.to_excel("AmazonWebScrapingPJ.xlsx", index=False)
