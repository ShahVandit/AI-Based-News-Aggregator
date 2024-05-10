from newspaper import Article

url = 'https://www.ndtv.com/india-news/netflix-indias-successful-business-model-leads-to-change-in-116-countries-3960645'
article = Article(url)
# print(article)

article.download()
article.parse()

print("author ",article.authors)
# ['Leigh Ann Caldwell', 'John Honway']

print(article.publish_date)
# datetime.datetime(2013, 12, 30, 0, 0)

print(article.text)
# 'Washington (CNN) -- Not everyone subscribes to a New Year's resolution...'
import nltk
# nltk.download('punkt')

print(article.top_image)

article.nlp()

# print(article.keywords)
# ['New Years', 'resolution', ...]
print('=============')
print(article.summary)

# scrapping -> aggregate -> 

# rss feed se link uthao(category ke sath) -> scrape karo (aggregate if possible) -> summarise