import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from services.users import fetchUsers, insertUser
from ui.articles import articles_index
from ui.categories import categories_index
from ui.groups import groups_index
from ui.operations import operation_index

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
        with st.sidebar.container():
            main_menu=option_menu("",["الرئيسية","المجموعات","الاصناف","العناصر","العمليات"])
        if main_menu == "الرئيسية":
            st.title("الرئيسية")
        elif main_menu == "المجموعات":
            groups_index()
        elif main_menu == "الاصناف":
            categories_index()
        elif main_menu == "العناصر":
            articles_index()
        elif main_menu =="العمليات":
            operation_index()
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