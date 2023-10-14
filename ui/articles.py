import streamlit as st


from services.articles import fetchArticles, insertArticle
from services.categories import fetchCategories
from services.helpers import formatNumber


def articles_index():
    st.title("العناصر")
    categories=[{"الصنف":article.category.title,
                 "التعيين":article.title,
                 "المدين":formatNumber(article.debit()),
                 "الدائن":formatNumber(article.credit()),
                 "الرصيد":formatNumber(article.balance())} for article in fetchArticles()]
    st.table(categories)
    articles_form(article=None)

def articles_form(article):
    with st.sidebar.form("category_form",clear_on_submit=True):
        category=st.selectbox("الاصناف", options=fetchCategories(),format_func=lambda c:c.title)
        title=st.text_input("", value='' if article ==None else article.title )
        submited=st.form_submit_button("حفظ")
        if submited:
            insertArticle(title,category)

