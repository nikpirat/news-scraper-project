import matplotlib.pyplot as plt

def plot_top_words(counter, n=10):
    common = counter.most_common(n)
    words, counts = zip(*common)
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.title("Top 10 most common words")
    plt.show()