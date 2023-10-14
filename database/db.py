import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.models import Base,User
BASE_DIR = os.path.dirname(os.path.relpath(__file__))
print(BASE_DIR)

connect_args = f"sqlite:///"+os.path.join(BASE_DIR, "personal-tools.sqlite")


engine = create_engine(connect_args)

Base.metadata.create_all(engine)

session = Session(engine)



# from deta import Deta
# from dotenv import load_dotenv
# import os
# import streamlit_authenticator as stauth
# load_dotenv('.env')
# DETA_KEY=os.getenv('DETA_KEY')
# deta=Deta(DETA_KEY)

# users=deta.Base('users')

# def insertUser(username,name,password):
#     return users.put({"key":username,"name":name,"password":password})

# def fetchUsers():
#     res=users.fetch()
#     return res.items
# def fetchUser(username):
#     return users.get(username)

# def updateUser(updates,username):
#     return users.update(updates,username)

# def deleteUser(username):
#     return users.delete(username)

#insertUser("admin","Mohamed",stauth.Hasher(['1111']).generate())

#deleteUser('admin')

#updateUser(updates={"password":stauth.Hasher(['1111']).generate()},username='admin')