import requests
import urls_to_track
import bs4
import re

temp_dic = {}

for i in urls_to_track.url:
    
    resp = requests.get(i)
    soup = bs4.BeautifulSoup(resp.content)
    prod_name = soup.find('h1').text
    prod_price = soup.find('div',['class','_30jeq3 _16Jk6d']).text
    prod_price_int = int(re.sub(r"[₹,]",'',prod_price))
    temp_dic[prod_name]=prod_price

print(temp_dic)

