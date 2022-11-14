import requests
import pandas as pd
from bs4 import BeautifulSoup

def get(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.text,'lxml')
    else:
        print('Error:', page.status_code)
        return None


def extract(soup):
    target = soup.find('div',class_= "_1YokD2 _3Mn1Gg")
    products = target.find_all('div' ,class_ = "_1AtVbE col-12-12" )
    print("products: ", len(products))
    info = []
    for item in products:
        name = item.find('div', class_= '_4rR01T')
        s_price = item.find('div', class_ = '_30jeq3 _1_WHN1')
        o_price = item.find('div', class_ = '_3I9_wc _27UcVY')
        rating = item.find('div', class_ = '_3LWZlK')
        rating_count = item.find('span', class_ = '_2_R_DZ') 
        data = {}
        try:
            data['name'] = name.text.strip()
        except:
            data['name'] = None
        try:
            data['s_price'] = s_price.text.strip()
        except:
            data['s_price'] = None
        try:
            data['o_price'] = o_price.text.strip()
        except:
            data['o_price'] = None
        try: 
            data['rating'] = rating.text.strip()
        except:
            data['rating'] = None
        try:
            data['rating_count'] = rating_count.text.strip()
        except:
            data['rating_count'] = None
        info.append(data)
        print('Extracted: ', name.text)
    return info

def save(data):
    if len(data) > 0:
        pd.DataFrame(data).to_csv('flipkart.csv', index = False)
    else:
        print('no data to save')

def main():
    pos = 1
    product = 'television'
    datalist = []
    while True:
    url = f'https://www.flipkart.com/search?q=television&page=1'
    soup = get(url)
    if soup:
        data = extract(soup)
        if data:
            datalist.extend(data)
            pos += 1
        else:
             break
        else:
             break
        save(datalist)
       
       
 main()