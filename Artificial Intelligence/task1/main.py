# Step 1: Import the necessary libraries

import nltk
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer

# Step 2: Download NLTK data

nltk.download('punkt')
nltk.download('vader_lexicon')

# Step 3: Define some sample texts

tweets = [
    "Just finished watching the new movie, it was amazing! #movienight 🎬",
    "The weather today is awful, I hate rainy days. ☔️",
    "Had a great experience at the restaurant, the food was delicious! 🍔"
]

# Step 4: Perform sentiment analysis using TextBlob

print("Sentiment analysis using TextBlob:")
for tweet in tweets:
    blob = TextBlob(tweet)
    sentiment = "positive" if blob.sentiment.polarity > 0 else "negative" if blob.sentiment.polarity < 0 else "neutral"
    print(f"Sentiment of '{tweet}': {sentiment}")

# Step 5: Perform sentiment analysis using NLTK

# Create SentimentIntensityAnalyzer instance
sia = SentimentIntensityAnalyzer()

print("\nSentiment analysis using NLTK:")
for tweet in tweets:
    scores = sia.polarity_scores(tweet)
    sentiment = "positive" if scores['compound'] > 0 else "negative" if scores['compound'] < 0 else "neutral"
    print(f"Sentiment of '{tweet}': {sentiment}")
