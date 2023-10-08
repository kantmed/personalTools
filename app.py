import streamlit as st
import streamlit_authenticator as stauth
from models import fetchUsers

users=fetchUsers()

usernames=[user['key'] for user in users]
names=[user['name'] for user in users]
passwords=[user['password'] for user in users]

credentials=list(map(lambda user:(
   {"usernames": {f'{user["key"]}':{'name':user['name'],'password':user['password']}}}
),users))[0]

auth=stauth.Authenticate(credentials=credentials,cookie_name="app",key="abcdf",cookie_expiry_days=30)

name,authentication_status,username=auth.login("Login","main")
if authentication_status ==False:
    st.error("Username/Password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
else :
    auth.logout("Logout","sidebar")
    st.title("الرئيسية")
    st.markdown(
        """
        <style>
            direction: rtl;
            background-color: coral;
        </style>
        """,
        unsafe_allow_html=True,
    )