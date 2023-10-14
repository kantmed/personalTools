from functools import reduce
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship,column_property
from sqlalchemy import Date, ForeignKey, Integer,String
from typing import List


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(String,nullable=False)
    username:Mapped[str]=mapped_column(String,nullable=False)
    password:Mapped[str]=mapped_column(String,nullable=False)
    email:Mapped[str]=mapped_column(String,nullable=True)

class Group(Base):
    __tablename__="groups"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(String,nullable=False)
    categories:Mapped[List["Category"]]=relationship("Category",back_populates="group")

class Category(Base):
    __tablename__="categories"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(String,nullable=False)
    group_id:Mapped[int]=mapped_column(Integer,ForeignKey("groups.id"))
    group:Mapped["Group"]=relationship("Group",back_populates="categories")
    articles:Mapped[List["Article"]]=relationship("Article",back_populates="category")

class Article(Base):
    __tablename__="articles"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    title:Mapped[str]=mapped_column(String,nullable=False)
    category_id:Mapped[int]=mapped_column(Integer,ForeignKey("categories.id"))
    category:Mapped["Category"]=relationship("Category",back_populates="articles")
    records:Mapped[List["Record"]]=relationship(back_populates="article",lazy="dynamic")

    def debit(self):
        return reduce(lambda x,y: x+y.debit ,self.records,0)
    def credit(self):
        return reduce(lambda x,y: x+y.credit ,self.records,0)
    def balance(self):
        return  reduce(lambda x,y: x+y.debit ,self.records,0)-reduce(lambda x,y: x+y.credit ,self.records,0) 
class Operation(Base):
    __tablename__="operations"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    number:Mapped[int]=mapped_column(Integer, nullable=False)
    type:Mapped[int]=mapped_column(Integer, nullable=False)
    date:Mapped[Date]=mapped_column(Date, nullable=False)
    records:Mapped[List["Record"]]=relationship(back_populates="operation")

class Record(Base):
    __tablename__="records"
    id:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    debit:Mapped[int]=mapped_column(Integer,default=0)
    credit:Mapped[int]=mapped_column(Integer,default=0)
    describe:Mapped[str]=mapped_column(String,nullable=True)
    article_id:Mapped[int]=mapped_column(Integer,ForeignKey("articles.id"))
    article:Mapped["Article"]=relationship(back_populates="records")
    operation_id:Mapped[int]=mapped_column(Integer,ForeignKey("operations.id"))
    operation:Mapped["Operation"]=relationship(back_populates="records")
