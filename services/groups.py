from database.db import session
from database.models import Group


def fetchGroups():
    return session.query(Group).all()

def insertGroup(title):
    group=Group(title=title)
    session.add(group)
    session.commit()