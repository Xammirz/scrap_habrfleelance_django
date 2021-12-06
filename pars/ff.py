
import requests
import json
from random import choice
from bs4 import BeautifulSoup as BS
import pprint

from requests.api import patch

url = "https://habr.com/ru/all"
headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]


jobs = []

def habr_parsing():
   
    
    url = "https://habr.com/ru/all"
    res = requests.get(url,headers=choice(headers))
    if res.status_code == 200:
            soup = BS(res.content, 'html.parser')
            ul = soup.find('div', class_='tm-articles-list')
            li = ul.find_all('a', class_="tm-article-snippet__title-link")
            
            for i in li:
                url = 'https://habr.com' + i['href']
                res = requests.get(url,headers=choice(headers))
                title = i.text
                
                
                if res.status_code == 200:
                    soup = BS(res.content, 'html.parser')
                    divs = soup.find_all('article', class_="tm-article-presenter__content tm-article-presenter__content_narrow")
                    information = soup.find_all('section', class_="tm-block tm-block_spacing-bottom")
                    ratings = soup.find_all('div', class_='tm-company-card__header')
                    icons = soup.find_all('div', class_='tm-data-icons tm-article-sticky-panel__icons')
                    user_content = soup.find_all('div', class_='tm-block__body tm-block__body_variant-balanced')
                    
                    

                    
                    for div in divs:
                        user = div.find('span', class_='tm-user-info tm-article-snippet__author').text
                        hab = div.find('div', class_='tm-article-snippet__hubs').text
                        body = div.find('div', id='post-content-body').text
                        time = div.find('span', class_='tm-article-snippet__datetime-published').text
                        teg = div.find('ul', class_='tm-separated-list__list').text
                        
                        try:  
                            image = div.find('img')['src']
                        except Exception as e:
                            image = "Не найдено"
                        
                        
                        
                            

                    for icon in icons:
                        try:
                            vote = icon.find('span', class_='tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_appearance-article tm-votes-meter__value_rating').text
                            bookmarks = icon.find('span', class_='bookmarks-button__counter').text
                            
                        except Exception as e:
                            vote = 0
                            bookmarks = 0
                            


                    for info in information:   
                        try:
                            info = info.find('div',class_='tm-company-basic-info').text
                        except Exception as e:
                            info = 'Не cуществует'
                        
                    

                    for us_content in user_content:
                        try:
                            user_content_karma = us_content.find('div', class_='tm-karma__votes tm-karma__votes_positive').text
                            user_content_rate = us_content.find('div', class_='tm-rating__header').text
                            contact = us_content.find('a', class_='tm-article-author__contact')['href']
                            contact2 = us_content.find('a', class_='tm-article-author__contact').text + contact
                            
                            
                        except Exception as e:
                            user_content_karma = 0
                            user_content_rate = 0
                            contact2 = 'Не найдено'
                        

                        
                    


                        
                        

                        
                            jobs.append({'url': url, 'title': title,
                                'teg': teg, 'body': body,'user': user, 'info' : info,
                                
                                'hab': hab, 'time': time,'image': image, 
                                'vote': vote, 
                                'bookmarks': bookmarks,
                                'contact2': contact2,
                                'user_content_karma': user_content_karma, 
                                'user_content_rate': user_content_rate
                                                })
    return jobs    