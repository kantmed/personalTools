import streamlit as st

from services.categories import fetchCategories, insertCategory
from services.groups import fetchGroups


def categories_index():
    st.title("المجموعات")
    categories=[{"المجموعة":category.group.title,"التعيين":category.title} for category in fetchCategories()]
    st.table(categories)
    categories_form(category=None)

def categories_form(category):
    with st.sidebar.form("category_form",clear_on_submit=True):
        group=st.selectbox("المجموعات", options=fetchGroups(),format_func=lambda g:g.title)
        title=st.text_input("", value='' if category ==None else category.title )
        submited=st.form_submit_button("حفظ")
        if submited:
            insertCategory(title,group)

