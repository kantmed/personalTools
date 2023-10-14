from database.db import session
from database.models import Operation


def fetchOperations():
    return session.query(Operation).all()

def insertOperation(number,type,date):
    session.add(Operation(number=number,type=type['key'],date=date))
    session.commit()

def fetchOperationByNumber(number):
    return session.query(Operation).where(Operation.number==number).first()

operationTypes=[{"key":1,"value":"صرف"},{"key":2,"value":"قبض"},{"key":3,"value":"تحويل"},{"key":4,"value":"اخر"}]