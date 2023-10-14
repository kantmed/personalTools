from database.db import session
from database.models import Record


def fetchRecords():
    return session.query(Record).all()

def insertRecord(debit,credit,describe,article,operation):
    session.add(Record(debit=debit,credit=credit,describe=describe,article_id=article.id,operation_id=operation.id))
    session.commit()

def fetchRecord(id):
    return session.query(Record).where(Record.id==id)