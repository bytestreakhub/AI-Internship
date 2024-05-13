import requests
import json
import pandas as pd

# Keyword Suggestor for Keyword Research

keyword=input('Add your keyword: ')
print("Top 10 Keywords:")

def api_call(keyword):
    
    keywords = [keyword]
     
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    response = requests.get(url, verify=False)
    suggestions = json.loads(response.text)
    
    
    for word in suggestions[1]:
        keywords.append(word)
        
    #functions for getting more kws, cleaning and search volume
    prefixes(keyword,keywords)
    suffixes(keyword,keywords)
    numbers(keyword,keywords)
    get_more(keyword,keywords)
    clean_df(keywords,keyword)
    
def prefixes(keyword,keywords):
    prefixes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','how','which','why','where','who','when','are','what']    
    
    for prefix in prefixes:
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + prefix + " " + keyword 
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        kws = suggestions[1]
        length = len(kws)
        
        for n in range(length):
            keywords.append(kws[n])
            
def suffixes(keyword,keywords):
    suffixes =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','like','for','without','with','versus','vs','to','near','except','has']
       
    for suffix in suffixes:
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword + " " + suffix 
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        kws = suggestions[1]
        length = len(kws)
        
        for n in range(length):
            keywords.append(kws[n])  
 
def numbers(keyword,keywords):
    for num in range(0,10):
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword + " " + str(num)
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        kws = suggestions[1]
        length = len(kws)
        
        for n in range(length):
            keywords.append(kws[n]) 

def get_more(keyword, keywords):
    count = 0
    for i in keywords:
        if count >= 10:
            break
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
        response = requests.get(url, verify=False)
        suggestions = json.loads(response.text)
        
        keywords2 = suggestions[1]
        length = len(keywords2)
                   
        for n in range(length):
            print(keywords2[n])
            count += 1
            if count >= 10:  # Print only top 10 keywords
                print('### Top 10 Keywords Reached ###')
                break

def clean_df(keywords,keyword):
    keywords = list(dict.fromkeys(keywords)) 

    new_list = [word for word in keywords if all(val in word for val in keyword.split(' '))]
    
    df = pd.DataFrame (new_list, columns = ['Keywords'])
     
    df.to_csv(keyword+'-keywords.csv')
                
    json_hist = df.to_json(orient="columns")
   
api_call(keyword)
