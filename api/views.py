# coding=utf8
# from googletrans import Translator
from translate import Translator
from .word_meaning import get_article
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 

from .models import Website

from .serializers import WebsiteSerializer,ArticleSerializer
# Create your views here.
from .summarizer import english_summary, hindi_summary, gujarati_summary
import requests
from bs4 import BeautifulSoup
# Summarization libraries
import nltk
import pandas as pd
import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from indicnlp.tokenize import sentence_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# from .filter_articles import filter_similer_articles

from .summarizer import english_summary, hindi_summary, gujarati_summary
import boto3
from .word_meaning import ndtv_search

from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

from dotenv import load_dotenv
load_dotenv()


import os

allArticles = []
# from lxml import etree # FOR XPATH
HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
                    'Accept-Language': 'en-US, en;q=0.5'})
def combine_feature(data):
    feature=[]
    for i in range(0,data.shape[0]):
        try:
            feature.append(data['title'][i]+' '+data['author'][i])
        except:
            pass
    return feature
def recommender(dictionary,currentArticle):
    # print(type(dictionary))
    # df=pd.DataFrame.from_dict(dictionary)
    
        
    df = pd.DataFrame(dictionary)
    df["author"]=""
    df = df.dropna(subset=['title','author'])
    title=currentArticle['title']  # insert main article title here
    df.reset_index(inplace = True)
    # Combining features
    df['combined']=combine_feature(df)
    cm=CountVectorizer().fit_transform(df['combined'])
    #Creating Cosine Similarity Matrix
    cs=cosine_similarity(cm)
    # unique_id = df[df.title==title]['id'].values[0]
    book_id=df.loc[df.title==title].index[0]
    scores=list(enumerate(cs[book_id]))

    sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
    ids=sorted_scores[-5:-1]
    dicts=[]
    for id in ids:
        dicts.append(pd.DataFrame.to_json(df.loc[id[0]]))
        # dicts.append(df.loc(id[0]))
    print(dicts)
    print(type(dicts))
    return dicts

def getnews18Articles(url):
    cnt=0
    global allArticles
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        articles=soup.find_all('item')
        singleArticle={
                        'title':"",
                        'image':"",
                        'publish_time':"",
                        'author_name':"",
                        'image_title':"",
                        'paragraphs':"",
                        }
        for article in articles:
            
            article_url = article.find('link').text
            date = article.find('pubDate').text
            # article
            # article_url=article.text
            resp = requests.get(article_url, headers=HEADERS)
            soup = BeautifulSoup(resp.content, 'html.parser')
            if(article_url != None):
                cnt=cnt+1
                arti = get_article(article_url)
                arti['date'] = date
                # print(arti+"\n")
                allArticles.append(arti)
            if cnt==4:
                return
    except Exception as e:
        print(e)
        # # title
        # title = soup.find('h1',{'class':'article_heading'})
        # if(title!=None):
        #     title = title.text.strip()
        #     singleArticle['title'] = title

        # # # image and caption
        # image = soup.find('figure',{'class':'jsx-771931618'})
        # if(image!=None):
        #     image_src=image.find('img')
        #     if(image_src != None):
        #         image = image_src['src']
        #         image_title = image_src['title']
                
        #         singleArticle['image'] = image.strip()
        #         singleArticle['image_title'] = image_title.strip()
            
        # # article
        # paragraph_content=[]
        # paragraphs = soup.find('article',{'class':'article-content-box'})
        # if(paragraphs!=None):
        #     pTag = paragraphs.find_all('p')
        #     if(pTag!=None):
        #         for p in pTag:
        #             if(len(p.text)>0):
        #                 paragraph_content.append(p.text.strip())
        #         if(len(paragraph_content)>1):
        #             singleArticle['paragraphs'] = "#".join(paragraph_content)
        #         elif len(paragraph_content)==1:
        #             singleArticle['paragraphs'] = paragraph_content[0]       


        # # author name and details
        # time = soup.find('div',{'class':'author_box_inner'})
        # if(time!=None):
        #     author_content = time.find('div',{'class':'author_content'})
        #     if(author_content!=None):
        #         author_url=author_content.find('a')
        #         if(author_url!=None):
        #             href= author_url['href'].strip()
        #             ind = href.find("@")
        #             href = href[0:ind]
        #             if(href.find(".")!=-1):
        #                 author_name = href.split(".")
        #                 mailTo = author_name[0].find(":")
        #                 author_name = author_name[0][mailTo+1:len(author_name[0])]+" "+author_name[1]
                        
        #             else:
        #                 name_ind = href.find(":")
        #                 author_name = href[name_ind+1 : len(href)].strip()
        #             singleArticle['author_name'] = author_name
        #         # publishing time
        # info=soup.find('div',{'class':'tags_outter'})
        # if(info!=None):
        #     ptym = info.find('div',{'class':'published_date'})
        #     if(ptym!=None):
        #         timeVal = ptym.text.strip()
        #         singleArticle['publish_time'] = timeVal
        #     uptym = info.find('div',{'class':'updated_date'})
        #     if(uptym!=None):
        #         upt = uptym.text.strip()
        #         if(len(upt)>0):
        #             singleArticle['publish_time'] = upt
        # if(singleArticle['title']!="" and singleArticle['paragraphs']!="" and singleArticle['image']!=""):
        #     allArticles.append(singleArticle)

def getNDTVArticles(url):
    cnt=0
    global allArticles
    try:
        content=[]
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        articles=soup.find_all('item')
        if(articles == None):
            return
        for article in articles:
            linkk = article.find('link')
            if(linkk == None):
                continue
            link = linkk.text
            date=""
            datee = article.find('pubDate')
            if(datee != None):
                date = datee.text
            if(link.find('-live-score-')==-1):
                cnt=cnt+1
                arti = get_article(link)
                arti['date'] = date
                allArticles.append(arti)
            if cnt==4:
                return
    except Exception as e:
        print(e)        
    # singleArticle={
    #                 'title':"",
    #                 'image':"",
    #                 'publish_time':"",
    #                 'author_name':"",
    #                 'image_title':"",
    #                 'paragraphs':"",
    #                 }
    # resp = requests.get(url)
    # soup = BeautifulSoup(resp.content, features="xml")
    # articles=soup.find_all('item')
    # article_links=[]
    # for article in articles:
    #     link = article.find('link').text
    #     if link.startswith('https://www.ndtv.com/video/'):
    #         continue
    #     webpage = requests.get(link, headers=HEADERS)
    #     soup = BeautifulSoup(webpage.content, "html.parser")
    #     # title
    #     try:
    #         title=soup.find('h1',{'class':'sp-ttl'}).text
    #         singleArticle['title'] = title.strip()
    #     except:
    #         continue
    #     # main content
    #     article_content=soup.find('div',{'class':'sp-cn ins_storybody'})
    #     if(article_content!=None):
    #         paragraphs=article_content.find_all('p')
    #         paragraph_content=[]
    #         for paragraph in paragraphs:
    #             paragraph_content.append(paragraph.text)
    #         if(len(paragraph_content)>1):
    #             singleArticle['paragraphs'] = "#".join(paragraph_content)
    #         elif len(paragraph_content)==1:
    #             singleArticle['paragraphs'] = paragraph_content[0].strip()
        
    #     else:
    #         continue
    #     # image
    #     image_tag=soup.find('div',{'class':'ins_instory_dv_cont'})
    #     if(image_tag!=None):
    #         try:
    #             imageInfo=image_tag.find('img')
    #             image = imageInfo['src']
    #             image_title = imageInfo['alt']
    #             singleArticle['image'] = image.strip()
    #             singleArticle['image_title'] = image_title.strip()
        
    #         except:
    #             image=None
    #     # publish time and date
    #     time_tag=soup.find('span',{'class':'pst-by_lnk'})
    #     if(time_tag != None):
    #         time=time_tag.find('span')
    #         if(time != None):
    #             timeVal = time.text.strip()
    #             singleArticle['publish_time'] = timeVal.strip()
        
            
    #     # author
    #     main_author_tag=soup.find('span',{'itemprop':'author'})
    #     if(main_author_tag != None):
    #         author_link=main_author_tag.find('meta')['content']
    #         author_name=main_author_tag.find('span').text
    #         singleArticle['author_name'] = author_name.strip()
        
        
        
    #     if(singleArticle['title']!="" and singleArticle['paragraphs']!="" and singleArticle['image']!=""):
    #         allArticles.append(singleArticle)

def getnewsTOIArticles(url):
    cnt=0
    global allArticles
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        articles=soup.find_all('item')
        if(articles == None):
            return
        for article in articles:
            article_url=article.find('link').text
            date = article.find('pubDate').text
            if(article_url.find('/articleshow/')!=-1):
                cnt=cnt+1
                arti = get_article(article_url)
                arti['date'] = date
                allArticles.append(arti)
            if cnt==4:
                return
    except Exception as e:
        print(e)        
    # content=[]
    # try:
    #     resp = requests.get(url)
    #     soup = BeautifulSoup(resp.content, features="xml")
    #     articles=soup.find_all('item')
    #     if(articles == None):
    #         return
        
    #     for article in articles:
    #         singleArticle={
    #                 'title':"",
    #                 'image':"",
    #                 'publish_time':"",
    #                 'author_name':"",
    #                 'image_title':"",
    #                 'paragraphs':"",
    #                 }
    #         article_url=article.find('link').text
    #         content.append(get_article("https://sports.ndtv.com/cricket/pbks-vs-rcb-live-score-ipl-2023-today-27th-match-punjab-kings-vs-royal-challengers-bangalore-live-score-updates-3964061"))
    #         print(content[0]['content'],content[0]['link'])
    #         print('---------------')
    #         if(article_url==None):
    #             continue
    #         resp = requests.get(article_url, headers=HEADERS)
    #         soup = BeautifulSoup(resp.content, 'html.parser')
            
    #         # title
    #         title = soup.find('h1',{'class':'_1Y-96'})
    #         if(title==None):
    #             title = soup.find('h1')
    #             singleArticle['title'] = title.text.strip()
    #         else:
    #             singleArticle['title'] = title.text.strip()
    #         # image and caption
    #         image = soup.find('div',{'class':'_3gupn'})
    #         if(image!=None):
    #             image_src=image.find('img')
    #             image = image_src['src']
    #             singleArticle['image'] = image.strip()
    #             singleArticle['image_title'] = image_src['alt'].strip()
    #         else:
    #             print()

    #         # article
    #         paragraphs = soup.find('div',{'class':'_3YYSt'})
    #         if(paragraphs!=None):
    #             singleArticle['paragraphs'] = paragraphs.text.strip()
                
    #         # publishing time
    #         # author name and details
    #         time = soup.find('div',{'class':'yYIu- byline'})
    #         if(time!=None):
    #             print(time.find('span').text)
    #             spanTime = time.find('span')
    #             if(spanTime!=None):
    #                 singleArticle['publish_time'] = spanTime.text.strip()
    #             aTag = time.find('a') 

    #             # problem
    #             if(aTag!=None):
    #                 author_url=time.find('a')
    #                 if(author_url!=None):
    #                     author_name=author_url.text.strip()
    #                     singleArticle['author_name'] = author_name

    #         if(singleArticle['title']!="" and singleArticle['paragraphs']!="" and singleArticle['image']!=""):
    #                 allArticles.append(singleArticle)
                   
    # except Exception as e:
    #     print(e)

def getPoliticsNews(url):
    cnt=0
    global allArticles
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        articles=soup.find_all('item')
        for article in articles:
            singleArticle={
                'title':"",
                'image':"",
                'publish_time':"",
                'author_name':"",
                'image_title':"",
                'paragraphs':"",
                }
            linkk = article.find('link')
            if(linkk==None):
                continue
            link = linkk.text
            date=""
            datee = article.find('pubDate')
            if(datee != None):
                date = datee.text
            webpage = requests.get(link, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "html.parser")
            if( link != None):
                cnt=cnt+1
                arti = get_article(link)
                arti['date'] = date
                allArticles.append(arti)
            if cnt==4:
                return
    except Exception as e: 
        print(e)


def getnews24Articles(url):
    cnt=0
    global allArticles
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, features="xml")
        articles=soup.find_all('item')
        for article in articles:
            singleArticle={
                'title':"",
                'image':"",
                'publish_time':"",
                'author_name':"",
                'image_title':"",
                'paragraphs':"",
                }
            linkk = article.find('link')
            if(linkk==None):
                continue
            link = linkk.text
            date=""
            datee = article.find('pubDate')
            if(datee != None):
                date = datee.text
            webpage = requests.get(link, headers=HEADERS)
            soup = BeautifulSoup(webpage.content, "html.parser")
            if( link != None):
                cnt=cnt+1
                arti = get_article(link)
                arti['date'] = date
                allArticles.append(arti)
            if cnt==4:
                return
            # # main article
            # page = soup.find_all('div',{'class': 'article tf-lhs-col'})
            
            # # posted time
            # articleTopBar = page[0].find("div",{'class':'article--top-bar'})
            # if(articleTopBar != None):
            #     postedDate = articleTopBar = articleTopBar.find('p')
            #     if(postedDate != None):
            #         singleArticle['publish_time'] = postedDate.text.strip()
          
            # # title
            # articleTitle = page[0].find('h1')
            # if(articleTitle != None):
            #     singleArticle['title'] = articleTitle.text.strip()
          
            # # compiled by
            # articleTop = page[0].find('div',{'class':'article--top'})
            # if(articleTop != None):
            #     compiler = articleTop.find('div',{'class':'article__details'})
            #     if(compiler != None):
            #         singleArticle['author_name'] = compiler.text.strip()
           
            # # article content
            # articleContent = page[0].find('div',{'class':'article-locked'})
            # if(articleContent != None):
            #     articleContentDiv = articleContent.find('div',{'class':'article__content'})
            #     if(articleContentDiv != None):
            #     # article image and caption
            #         articleImage = articleContentDiv.find("div",{'class':'article__featured-image'})
            #         if(articleImage != None):
            #             url = articleImage.img['src']
            #             if(url != None):
            #                 image_url = url.strip()
            #                 singleArticle['image'] = image_url
            #             caption = articleImage.find('div',{'class':'caption'})
            #             if(caption != None):
            #                 singleArticle['image_title'] = caption.text.strip()
              
            #         # main article content
            #         content = articleContentDiv.find('div',{'class':'article__body'})
            #         if(content != None):
            #             pTag = content.find_all('p')
            #             if(pTag != None):
            #                 allPara = []
            #                 for p in pTag:
            #                     if(len(p.text)>0):
            #                         allPara.append(p.text.strip())
            #                 if(len(allPara)>1):
            #                     singleArticle['paragraphs'] = "#".join(allPara)
            #                 elif len(allPara)==1:
            #                     singleArticle['paragraphs'] = allPara[0].strip()
                            
            # if(singleArticle['title']!="" and singleArticle['paragraphs']!="" and singleArticle['image']!=""):
            #     allArticles.append(singleArticle)
    except Exception as e: 
        print(e)


@api_view(["POST"])
def recommendation(request):
    data = JSONParser().parse(request)
    articles = data['articles']
    currentArticle = data['currentArticle']
    recommend_article = recommender(articles,currentArticle)
    print(recommend_article)
    return Response(recommend_article)

@api_view(["GET"])
def fetchArticles(request,category=None):
    global allArticles
    allArticles=[]
    if(category == None):
        return Response({"error":"Select any category to fetch articles"})
    if(category.find(" ")!=-1):
        category = category.lower().split(" ").join("-")
    else:
        category = category.lower()
    
    links = Website.objects.filter(category = category)
    for link in links:
        print(link.newsWebsiteName + " ---- "+ link.link)
        
        if link.newsWebsiteName == "times-of-india":
            getnewsTOIArticles(link.link)
        elif link.newsWebsiteName == "ndtv" :
            getNDTVArticles(link.link)
        elif link.newsWebsiteName == "news18":
            getnews18Articles(link.link)
        elif link.newsWebsiteName == "news24" or link.newsWebsiteName=="the-hindu":
            getnews24Articles(link.link)
        elif link.newsWebsiteName == "politics":
            getPoliticsNews(link.link)
            print("Bhavya ")
    # serializer = ArticleSerializer(allArticles , many=True)
    print(len(allArticles))
    # filter_articles=filter_similer_articles(allArticles)
    return Response(allArticles)

@api_view(['GET'])
def fetchArticleByNews(request,websiteName=None):
    if(websiteName==None):
        return Response({"error":"Select any category to fetch articles"})
    links = Website.objects.filter(newsWebsiteName = websiteName)
    if(links[0].newsWebsiteName == "news24"):
        getnews24Articles(links[0].link)
    elif links[0].newsWebsiteName == "ndtv":
        getNDTVArticles(links[0].link)
    elif links[0].newsWebsiteName == "news18":
        getnews18Articles(links[0].link)
    elif links[0].newsWebsiteName == "times-of-india":
        getnewsTOIArticles(links[0].link)
    # serializer = ArticleSerializer(allArticles , many=True)
    return Response(allArticles)


# language translator
@api_view(['POST'])
def translator(request):
    translatedArticles = []
    data = JSONParser().parse(request)
    # print(data)
    language = data['language']
    articles = data['articles']
    cur_lang = data['cur_lang']

    lang = language[0:2].lower()
    
    cur = cur_lang[0:2].lower()
    # translator = Translator()
    translate = boto3.client(service_name='translate', region_name='ap-south-1',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'), use_ssl=True)
    for i in range(len(articles)):
        singleArticle = articles[i]
        
        art=dict()
        try:
            for key,value in singleArticle.items():
                if(key=="publish_date" or key=='link' or key=='media' or key=="extra_images" or value=="" or value==None): #publishedAt
                    art[key] = value
                    continue
                val = translate.translate_text(Text=str(value),
                                SourceLanguageCode=cur,
                                TargetLanguageCode=lang)
                art[key] = val['TranslatedText']
            translatedArticles.append(art)
        
        except Exception as e:
            print(e)
            
    
    return Response(translatedArticles)

# news summarizer
@api_view(['Post'])
def articleSummarizer(request):
    data = JSONParser().parse(request)
    content = data['content']
    language = data['language']
    summarize_content = ""
    if(language=='English'):
        summarize_content = english_summary(content)
    elif (language=='Hindi'):
        summarize_content = hindi_summary(content)
    else:
        summarize_content = gujarati_summary(content)
    return Response(summarize_content)

# search news
@api_view(['Post'])
def searchArticles(request):
    try:
        data = JSONParser().parse(request)
        searchText = data['searchText']
        print(searchText)
        searchArticles = ndtv_search(searchText) 
        print(searchArticles)
        return Response(searchArticles)
    except Exception as e:
        return Response(e)
    
@api_view(['Post'])
def SCRAPE(request):
    try:
        data = JSONParser().parse(request)
        articles = data['articles']
        for arti in articles:
            scrape_article = get_article(arti['link'])
            arti['content'] = scrape_article['content']
        print(articles)
        return Response(articles)
    except Exception as e:
        return Response(e)

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
            })
        except Exception as e:
            return Response("Something wrong happen, Please try again...")
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            return super(LoginAPI, self).post(request, format=None)
        except Exception as e:
            return Response("Invalid Credentials...")