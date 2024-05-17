import wikipedia
from response import chatbot
from googleapiclient.discovery import build

API_KEY = 'AIzaSyBETPim_nPRc1hePgB1IdVZxkv1dhvHE1s'
SEARCH_ENGINE_ID = '13a776ef6ff6b42f5'

service = build('customsearch', 'v1', developerKey=API_KEY)

def fetch_google_search(query):
    result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()
    items = result['items'] if 'items' in result else []
    return [item['link'] for item in items]

def fetch_wikipedia_summary(query):
    try:
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, provide options
        return f"Disambiguation Error: {', '.join(e.options)}"
    except wikipedia.exceptions.PageError:
        # If no Wikipedia page found for the query
        return None

print("Welcome! Ask me anything or say goodbye to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    elif user_input.lower().startswith('search'):
        query_parts = user_input.split(' ', 1)
        if len(query_parts) == 2:
            query = query_parts[1]
            search_results = fetch_google_search(query)
            if search_results:
                print("Bot: Here are some search results:")
                for link in search_results:
                    print(link)
            else:
                print("Bot: Sorry, I couldn't find any results for that query.")
    elif user_input.lower().startswith('wiki'):
        query = user_input.split(' ', 1)[1]
        summary = fetch_wikipedia_summary(query)
        if summary:
            print("Bot: Here's a summary from Wikipedia:")
            print(summary)
        else:
            print("Bot: Sorry, I couldn't find any information on that topic.")
    else:
        response = chatbot.respond(user_input)
        print("Bot:", response)
