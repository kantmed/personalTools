import streamlit as st

from services.groups import fetchGroups, insertGroup


def groups_index():
    st.title("المجموعات")
    groups=[{"التعيين":group.title} for group in fetchGroups()]
    st.table(groups)
    groups_form(group=None)

def groups_form(group):
    with st.sidebar.form("group_form",clear_on_submit=True):
        title=st.text_input("", value='' if group ==None else group.title )
        submited=st.form_submit_button("حفظ")
        if submited:
            insertGroup(title)

