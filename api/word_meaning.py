import requests
from bs4 import BeautifulSoup
# from .summarizer import english_summary
from newspaper import Article
import warnings
warnings.filterwarnings("ignore")
def get_article(article_link):
    try:
        article = Article(article_link)
        article.download()
        article.parse()
        article_details={}
        # elif:
        article_details.update({'content':article.text})
        return article_details
    except Exception as e:
        return {'content':""}

url='https://www.ndtv.com/search?searchtext='
def ndtv_search(searchText):
    content=[]
    resp = requests.get(url+searchText)
    soup = BeautifulSoup(resp.content, features="html")
    lists=soup.find_all('div',{'class':'src_itm-ttl'})
    dates=soup.find_all('span',{'class':'src_itm-stx'})
    # print(dates[0].text.split('|')[1])
    if(len(lists)==0):
        return 'No results found'
    cnt=0
    for it in lists:
        # date=it.find('span',{'class':'src_itm-stx'}).text
        # print(date)
        print(it.find('a')['href'])
        arti=get_article((it.find('a')['href']))
        arti['date']=dates[cnt].text.split('|')[len(dates[cnt].text.split('|'))-1].strip()
        content.append(arti)
        cnt=cnt+1
        # print(content)
        # content.append({get_article((it.find('a')['href'])), date=date[i].text.split('|')[1].strip()})
    return content



def get_ndtv_links(rss_link):
    resp = requests.get(rss_link)
    soup = BeautifulSoup(resp.content, features="xml")
    articles=soup.find_all('item')
    if(articles == None):
        return
    article_links=[]
    for article in articles:
        link = article.find('link').text
        if(link.find('-live-score-')==-1):
            print(link)
        article_links.append(link)
    return article_links
# get_ndtv_links('https://feeds.feedburner.com/ndtvsports-latest')
def get_toi_links(rss_link):
    resp = requests.get(rss_link)
    soup = BeautifulSoup(resp.content, features="xml")
    articles=soup.find_all('item')
    if(articles == None):
        return
    
    for article in articles:
        article_url=article.find('link').text
        if(article_url.find('/articleshow/')!=-1):
            print(article_url)
    return 
# get_toi_links('https://timesofindia.indiatimes.com/rssfeeds/4719148.cms')
# scrapping
# (get_article('https://www.news18.com/cricketnext/ipl-2023-kkr-coach-chandrakant-pandit-eyes-massive-turnaround-ahead-of-second-half-7647241.html'))
# article_summary=english_summary()
# print(ndtv_search(url))