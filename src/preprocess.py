import re
import nltk
from nltk.corpus import stopwords, words

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text) # Regular expressions to remove punctuation and special characters.
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')] # Creates a new list of tokens where all stopwords have been removed.
    return ' '.join(tokens)