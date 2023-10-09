from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey, Integer,String
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