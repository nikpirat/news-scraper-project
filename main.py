from src.scraper import scrape_articles
from src.preprocess import clean_text
from src.analyze import get_word_frequencies
from src.visualize import plot_top_words

def main():
    urls = [
        'https://www.bbc.com/news/articles/c9dgpjqg12lo',
        'https://www.bbc.com/news/articles/cq53l41gl8jo',
        'https://www.bbc.com/news/articles/cvg9r4q99g4o',
        'https://www.bbc.co.uk/news/resources/idt-868e3c3d-25ec-43cb-bcc0-8832464b91ca',
        'https://www.bbc.com/news/articles/cvg86pd63j8o'
    ]

    # Scrape
    df = scrape_articles(urls)

    # Preprocess
    df['cleaned'] = df['text'].apply(clean_text)

    # Analyze
    counter = get_word_frequencies(df['cleaned'])

    # Visualize
    plot_top_words(counter)

if __name__ == '__main__':
    main()