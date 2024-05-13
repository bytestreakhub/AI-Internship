# Import necessary libraries
import requests
import json
import pandas as pd

# Prompt user to input a keyword
keyword=input('Add your keyword: ')

# Print a message indicating that the top 10 keywords will be printed
print("Top 10 Keywords:")

# Define a function to make API calls and gather keyword suggestions
def api_call(keyword):
    # Initialize a list to store keywords
    keywords = [keyword]
     
    # Construct the URL for the initial API call
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword
    # Make the API call
    response = requests.get(url, verify=False)
    # Parse the JSON response
    suggestions = json.loads(response.text)
    
    # Extract suggestions from the response and append them to the list of keywords
    for word in suggestions[1]:
        keywords.append(word)
        
    # Call helper functions to gather more keyword suggestions
    prefixes(keyword, keywords)
    suffixes(keyword, keywords)
    numbers(keyword, keywords)
    get_more(keyword, keywords)
    clean_df(keywords, keyword)

# Define a function to gather keyword suggestions with prefixes
def prefixes(keyword, keywords):
    # Define a list of prefixes to try
    prefixes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','how','which','why','where','who','when','are','what']    
    
    # Iterate over each prefix
    for prefix in prefixes:
        # Construct the URL for the API call with the prefix
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + prefix + " " + keyword 
        # Make the API call
        response = requests.get(url, verify=False)
        # Parse the JSON response
        suggestions = json.loads(response.text)
        
        # Extract suggestions from the response and append them to the list of keywords
        for word in suggestions[1]:
            keywords.append(word)

# Define a function to gather keyword suggestions with suffixes
def suffixes(keyword, keywords):
    # Define a list of suffixes to try
    suffixes =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','y','x','y','z','like','for','without','with','versus','vs','to','near','except','has']
    
    # Iterate over each suffix
    for suffix in suffixes:
        # Construct the URL for the API call with the suffix
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword + " " + suffix 
        # Make the API call
        response = requests.get(url, verify=False)
        # Parse the JSON response
        suggestions = json.loads(response.text)
        
        # Extract suggestions from the response and append them to the list of keywords
        for word in suggestions[1]:
            keywords.append(word)

# Define a function to gather keyword suggestions with numbers
def numbers(keyword, keywords):
    # Iterate over numbers from 0 to 9
    for num in range(0,10):
        # Construct the URL for the API call with the number
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + keyword + " " + str(num)
        # Make the API call
        response = requests.get(url, verify=False)
        # Parse the JSON response
        suggestions = json.loads(response.text)
        
        # Extract suggestions from the response and append them to the list of keywords
        for word in suggestions[1]:
            keywords.append(word) 

# Define a function to gather more keyword suggestions
def get_more(keyword, keywords):
    # Initialize a counter to keep track of the number of keywords gathered
    count = 0
    # Iterate over each keyword
    for i in keywords:
        # If the top 10 keywords have been reached, exit the loop
        if count >= 10:
            break
        # Construct the URL for the API call with the keyword
        url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + i
        # Make the API call
        response = requests.get(url, verify=False)
        # Parse the JSON response
        suggestions = json.loads(response.text)
        
        # Extract suggestions from the response and print them
        keywords2 = suggestions[1]
        length = len(keywords2)
                   
        for n in range(length):
            print(keywords2[n])
            count += 1
            # If the top 10 keywords have been reached, print a message and exit the loop
            if count >= 10:
                print('### Top 10 Keywords Reached ###')
                break

# Define a function to clean the list of keywords and save it to a CSV file
def clean_df(keywords, keyword):
    # Remove duplicates from the list of keywords
    keywords = list(dict.fromkeys(keywords)) 
    # Filter out keywords that do not contain the primary keyword
    new_list = [word for word in keywords if all(val in word for val in keyword.split(' '))]
    
    # Convert the list of keywords to a DataFrame
    df = pd.DataFrame (new_list, columns = ['Keywords'])
     
    # Save the DataFrame to a CSV file
    df.to_csv(keyword+'-keywords.csv')
                
    # Convert the DataFrame to a JSON object
    json_hist = df.to_json(orient="columns")
   
# Call the api_call function to start the keyword suggestion process
api_call(keyword)
