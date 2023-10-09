from database.db import session
from database.models import User
import streamlit_authenticator as stauth




def fetchUsers():
    return session.query(User).all()

def insertUser(name,username,password,email):
    user=User(username=username,name=name,email=email,password=stauth.Hasher([password]).generate()[0])
    session.add(user)
    session.commit()