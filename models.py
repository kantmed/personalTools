from deta import Deta
from dotenv import load_dotenv
import os
import streamlit_authenticator as stauth
load_dotenv('.env')
DETA_KEY=os.getenv('DETA_KEY')
deta=Deta(DETA_KEY)

users=deta.Base('users')

def insertUser(username,name,password):
    return users.put({"key":username,"name":name,"password":password})

def fetchUsers():
    res=users.fetch()
    return res.items
def fetchUser(username):
    return users.get(username)

def updateUser(updates,username):
    return users.update(updates,username)

def deleteUser(username):
    return users.delete(username)

#insertUser("admin","Mohamed",stauth.Hasher(['1111']).generate())

#deleteUser('admin')

#updateUser(updates={"password":stauth.Hasher(['1111']).generate()},username='admin')