# Import the necessary library
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the NLTK data files (you only need to do this once)
nltk.download('punkt')

# Define a sample text
sample_text = "Hello, students! Welcome to the world of Natural Language Processing. NLTK makes it fun and easy to analyze text."

# Tokenize the text into sentences
sentences = sent_tokenize(sample_text)
print("Sentences:", sentences)

# Tokenize the text into words
words = word_tokenize(sample_text)
print("Words:", words)

# Count the number of sentences
num_sentences = len(sentences)
print("Number of sentences:", num_sentences)

# Count the number of words
num_words = len(words)
print("Number of words:", num_words)
