import nltk

# To use NLTK data files, you need to download them first. This can be done using the NLTK downloader
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('movie_reviews')
nltk.download('reuters')

#Once downloaded, you can import and use these resources in your NLP projects.

# Here are some commonly used NLTK data files and their specific uses:

# 1) WordNet - Provides synonyms, antonyms, definitions, and usage examples for English words.
from nltk.corpus import wordnet as wn
syns = wn.synsets("program")
print(syns[0].definition())

# 2) Stopwords - Provides a list of common stop words that can be filtered out of text data to reduce noise.
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
words = ["this", "is", "a", "sample", "sentence"]
filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)

# 3) Punkt - A pre-trained model for sentence tokenization.
from nltk.tokenize import sent_tokenize
text = "Hello, world. How are you?"
sentences = sent_tokenize(text)
print(sentences)

# 4) Movie Reviews - Used for sentiment analysis and text classification tasks.
from nltk.corpus import movie_reviews
positive_ids = movie_reviews.fileids('pos')
negative_ids = movie_reviews.fileids('neg')

# 5) Reuters - A collection of news articles used for topic classification and text categorization tasks.
from nltk.corpus import reuters
print(reuters.fileids()[:10])