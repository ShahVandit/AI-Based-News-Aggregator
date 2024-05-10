import re
import spacy
import pandas as pd
import numpy as np
import time
# Step 1: Get links and contents
# Use approx top 10 or so from headline section on homepages of
# Guardian, NYT, BBC News, Reuters
# See get-article-texts.py for implementation
article_texts=[]
i=1
df=pd.read_csv('articles.csv')
article_texts=df['title'].tolist()


# Step 2: Named entity recognition
time.sleep(5)
nlp = spacy.load("en_core_web_sm")
all_entities_listol = [] #list of lists
for t in article_texts:
    doc = nlp(t)
    article_entities = []
    for ent in doc.ents:
        if (ent.text.lower() not in article_entities) and (len(ent.text.lower())>1):
            article_entities.append(ent.text.lower())  
    all_entities_listol.append(sorted(article_entities))
# Note that there are often several entities that are effectively the same 
# e.g. Boris Johnson, the prime minister, Mr.Johnson
# group these with e.g. word2vec?







# Step 3: tf-idf vectorizer
# Aim to have, for each article, a vector of size = #(all named entities)
# Each element of the vector corresponds to the tf-idf value for a particular named entity

# Step 3a: Vocab and corpus
# Vocab is all the named entities
vocab = []
for article_entities in all_entities_listol:
    for entity in article_entities:
        if (entity.lower() not in vocab):
            vocab.append(entity.lower()) #lowercase for CountVectorizer
vocab=sorted(vocab)

# See reuters-corpus.py for the implementation of getting corpus
f = open('reuters-corpus-10k-text.txt', encoding="utf-8")
docs = re.split(r'\n{4}',f.read()) #\n\n\n\n splits the articles in the corpus file f
docs = docs[:-1] #remove final empty string
# Step 3b: Compute idf values (using corpus)
# First get counts in corpus of vocab words/phrases
from sklearn.feature_extraction.text import CountVectorizer
# Set vocab and limit to phrases of 1-4 tokens, then get document-term matrix
cv1 = CountVectorizer(vocabulary=vocab, analyzer = 'word', ngram_range=(1,4))
corpus_vocab_count_matrix = cv1.transform(docs)
# N.B.: Vocab is ONLY named entities from original ~50 articles
# corpus_vocab_count_matrix is sparse matrix, row=(article in corpus) and column=(word in vocab)
# print(corpus_vocab_count_matrix.shape) shows corpus is 10k articles, vocab ~1k phrases
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transformer.fit(corpus_vocab_count_matrix)
# #to see idf values, put in data frame
# df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv1.get_feature_names(), columns=['idf-weights'])
# df_idf = df_idf.sort_values(by=['idf-weights'])
# print(df_idf.head(10)) #shows idf weights of most common in the corpus of the ~1k 'vocab' 



# Step 3c: Compute tfidf values for each article

# analyzer='word' runs faster, but issues with vocab with punctuation e.g. O'Neill
#   BUT 'char' matches e.g. 'UN' and 'US' incorrectly in words like 'under' and 'useful'
# cv2 = CountVectorizer(vocabulary=vocab, analyzer = 'char', ngram_range=(1,30))

articles_vocab_count_matrix = cv1.transform(article_texts)
#avcm = np.asarray(articles_vocab_count_matrix.todense())
tfidf_matrix = tfidf_transformer.transform(articles_vocab_count_matrix)
tfidf_array = np.asarray(tfidf_matrix.todense()) #NB change from numpy matrix to array

# See tfidf for first article
df = pd.DataFrame(tfidf_array[0], index=cv1.get_feature_names_out(), columns=['tfidf'])
df_descending = df.sort_values(by=['tfidf'], ascending=False)
print(df_descending.head(5))

# # See top vocab for each article
# most_important_vocabs=[]
# for row in tfidf_array:
#     most_important_vocab = most_important_vocabs.append(vocab[np.where(row==max(row))[0][0]])
# print(most_important_vocabs)

# NB: some of vocab are NOT in entities for the article, but still have tfidf>0
#   ---named entity recognition isn't perfect...
# dfindices = [df.index[i] for i in range(len(vocab)) if df.iloc[i]['tfidf']>0]
# print('tfidf!=0 but not in entity list', [w for w in dfindices if w not in all_entities_listol[0]])
# print('in ent list but tfidf=0', [w for w in all_entities_listol[0] if w not in dfindices])






# Step 4: Clustering
# We now have a 'description' of each article with its tfidf vector
# Want to put together similar news articles
#   Want to predict a category, with an unknown number of categories, with unlabelled data
#   -DBSCAN is a good choice here

# Compare each of the ~50 tfidf vectors
#   -high-dimensional so use cosine similarity (not L2) to help avoid curse of dimensionality
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine
distance_array = pairwise_distances(tfidf_array, metric='cosine')
# print(distance_array[12])

from sklearn.cluster import DBSCAN
#around .6 or .65 seems to work well
clustering = DBSCAN(eps=0.6, min_samples=2, metric='precomputed').fit(distance_array)
for i in range(max(clustering.labels_)):
    print(np.where(clustering.labels_==i)[0])

### Performs very poorly
# from sklearn.cluster import SpectralClustering
# clustering = SpectralClustering(n_clusters=20, affinity = 'precomputed').fit(similarity_array)
# for i in range(20):
#     print(np.where(clustering.labels_==i))
