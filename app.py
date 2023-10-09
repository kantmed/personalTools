import streamlit as st
import streamlit_authenticator as stauth
from services.users import fetchUsers, insertUser

users=fetchUsers()

if users:

    # usernames=[user for user in users]
    # names=[user['name'] for user in users]
    # passwords=[user['password'] for user in users]

    credentials=list(map(lambda user:(
    {"usernames": {f'{user.username}':{'name':user.name,'password':user.password}}}
    ),users))[0]

    auth=stauth.Authenticate(credentials=credentials,cookie_name="app",key="abcdf",cookie_expiry_days=30)

    name,authentication_status,username=auth.login("Login","main")
    if authentication_status ==False:
        st.error("Username/Password is incorrect")
    elif authentication_status == None:
        st.warning("Please enter your username and password")
    else :
        auth.logout("Logout","sidebar")
        st.sidebar.subheader("مرحبا بك " + st.session_state.name)
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
else:
    with st.form("register_form",clear_on_submit=True):
        name=st.text_input("الاسم")
        username=st.text_input("اسم المستعمل")
        email=st.text_input("العنوان البريدي")
        password=st.text_input("كلمة السر",type="password")
        submited=st.form_submit_button("حفظ")
        if submited:
            insertUser(name,username,password,email)
            st.success("تمت العملية بنجاح")