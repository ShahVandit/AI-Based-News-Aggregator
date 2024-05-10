import boto3
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
# translate = boto3.client(service_name='translate', region_name='ap-south-1',aws_access_key_id='AKIAZSEAAAEC4VR3J6NE', aws_secret_access_key='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', use_ssl=True)
# result = translate.translate_text(Text="Today is Sunday...",
#                                   SourceLanguageCode="en",
#                                   TargetLanguageCode="hi")
# print(f'TranslatedText: {result["TranslatedText"]}')

def combine_feature(data):
    feature=[]
    for i in range(0,data.shape[0]):
        try:
            feature.append(data['title'][i])
        except:
            pass
    return feature

def filter_similer_articles(dicti):
    df=pd.DataFrame(dicti)
    # df['author']=''
    features=combine_feature(df)
    cm=CountVectorizer().fit_transform(features)
    #Creating Cosine Similarity Matrix
    # cs=cosine_similarity(cm)
    similarity_values = pd.DataFrame(cosine_similarity(cm))
    sm =cosine_similarity(cm)
    # print(sm[1])
    indics=[]
    for _, row in similarity_values[similarity_values <= 0.8].iterrows():
        # print(row)
        # print('..')
        x=similarity_values.columns[row.isnull()].tolist()
        indics.append(x)
           

    *y,=map(list,{*map(tuple,indics)})
    unique_ids=[]
    for x in y:
        unique_ids.append(x[0])
    newDf= (df.iloc[unique_ids])

    dicts=newDf.to_dict()
    return (dicts)

    # print(similarity_values.columns[row.isnull()].tolist())
    # print(similarity_values)
    # print(sm.shape)
    # for row in sm:
    #     for col in row:
    #         print(col)
    #         print('-----------')
    #     print(row)
    # similarity_values = pd.DataFrame(cosine_similarity(cm)<0.80)
    # arr=set()
    # for i in range(0,len(similarity_values[0])):
    #     for j in range(i,len(similarity_values[1])):
    #         if((similarity_values.iloc[i,j])==False):
    #             if(i==j):
    #                 arr.add(j)
                    # similarity_values.drop(j, axis='columns')
    # print(arr)
            # print(similarity_values.loc[similarity_values[j]==True])
            # print('fsdf')
    # print(for_rows)
    # print(similarity_values)
    # for row in similarity_values:
    #     similarity_values=similarity_values[similarity_values[row]!=True]
            
    # print(similarity_values)
    # print(cs.shape)
    return
# filter_similer_articles()