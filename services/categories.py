from database.db import session
from database.models import Category


def fetchCategories():
    return session.query(Category).all()

def insertCategory(title,group):
    category=Category(title=title,group_id=group.id)
    session.add(category)
    session.commit()