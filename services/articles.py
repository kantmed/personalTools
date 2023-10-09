from database.db import session
from database.models import Article


def fetchArticles():
    return session.query(Article).all()

def insertArticle(title,category):
    article=Article(title=title,category_id=category.id)
    session.add(article)
    session.commit()