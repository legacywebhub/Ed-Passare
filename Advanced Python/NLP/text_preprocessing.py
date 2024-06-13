# Import the necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download the NLTK data files (you only need to do this once)
nltk.download('punkt')
nltk.download('stopwords')

# Define a sample text
sample_text = "Hello, students! Welcome to the world of Natural Language Processing. NLTK makes it fun and easy to analyze text."

# Step 1: Convert text to lowercase
text_lower = sample_text.lower()
print("Lowercase Text:", text_lower)

# Step 2: Tokenize the text into words
words = word_tokenize(text_lower)
print("Tokenized Words:", words)

# Step 3: Remove punctuation (keep only alphabetic tokens)
words = [word for word in words if word.isalpha()]
print("Words without Punctuation:", words)

# Step 4: Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]
print("Filtered Words:", filtered_words)

# Step 5: Perform stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("Stemmed Words:", stemmed_words)
