# Import the necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Initialize the Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Define some sample texts
texts = [
    "I love this product! It's amazing and works perfectly.",
    "This is the worst experience I've ever had. Very disappointed.",
    "The movie was okay, not great but not bad either.",
    "I'm so happy with the service I received.",
    "I hate waiting in long lines. It's so frustrating."
]

# Analyze the sentiment of each text
for text in texts:
    sentiment = sia.polarity_scores(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}\n")
