import pandas as pd
from collections import Counter

def get_word_frequencies(texts):
    all_words = ' '.join(texts).split()
    return Counter(all_words)