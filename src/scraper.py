from newspaper import Article
import pandas as pd

def scrape_articles(urls):
    articles = []
    for url in urls:
        article = Article(url)
        article.download()
        article.parse()
        articles.append({
            'title': article.title,
            'text': article.text,
            'date': article.publish_date,
        })
    return pd.DataFrame(articles)