import pandas as pd
from bs4 import BeautifulSoup
import requests 

#1. get the webpage as soup
#2. extract the data
#3. save the data
#4. bind everything together

def  get(url):
    page = requests.get(url)
    if page.status_code == 200:
        return BeautifulSoup(page.text, 'lxml')
    else:
        print('Error:', page.status_code) 
        return None
           
def extract(soup):
    target = soup.find('div', class_ = 'lisingNews')
    news = target.find_all('div', class_ = 'newsItm')
    if len(news) > 0 :
        data = [] # list of dict 
        for item in news :
            title = item.find('h2', class_ = 'newsHdng')
            source = item.find('span', class_='posted-by')
            summary = item.find('p', class_ = 'newsCont')
            data.append({
                'title': title.text,
                'source': source.text,
                'summary': summary.text
            })
          return data


def save(data_list):
    if len(data_list) > 0:
        pd.DataFrame(data_list).to_csv('headlines.csv', index)