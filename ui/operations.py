import streamlit as st
from functools import reduce
from services.articles import fetchArticles
from services.operations import fetchOperationByNumber, fetchOperations, insertOperation, operationTypes
from services.records import insertRecord

current=0
def operation_index():
    st.subheader("العمليات")
    operation_form()
    record_form()
    for operation in fetchOperations():
        debits=reduce(lambda x,y: x + y.debit,operation.records,0)
        credits=reduce(lambda x,y: x + y.credit,operation.records,0)

        with st.container():
            col1,col2,col3,col4=st.columns(4)
            col1.text(operation.number)
            col2.text(operation.date)
            col3.text(debits)
            col4.text(credits)
            st.table([{"التعيين":record.article.title,"المدين":record.debit,"الدائن":record.credit,"التبرير":record.describe if record.describe != None else ''} for record in operation.records])

def operation_form():
    operation=fetchOperations()[-1]
    with st.form("operation_form",clear_on_submit=True):
        col1,col2,col3=st.columns(3)
        number=col1.text_input("رقم العملية",value=operation.number+1)
        type=col2.selectbox("نوع العملية",options=operationTypes,format_func=lambda t:t["value"])
        date=col3.date_input("تاريخ العملية")
        submited=st.form_submit_button("حفظ")
        if submited:
           insertOperation(number,type,date)

def record_form():
    operation=fetchOperations()[-1]
    with st.sidebar.form("record_form",clear_on_submit=True):
        number=st.text_input("رمز العملية",value=operation.number,disabled=True)
        debit=st.text_input("المدين")
        credit=st.text_input("الدائن")
        describe=st.text_input("التبرير")
        article=st.selectbox("العناصر",options=fetchArticles(),format_func=lambda a:a.title)
        submited=st.form_submit_button("حفظ")
        if submited:
            operation=fetchOperationByNumber(number)
            debits=reduce(lambda x,y: x + y.debit,operation.records,0)
            credits=reduce(lambda x,y: x + y.credit,operation.records,0)
            if debits + credits == 0 or debits != credits :
                insertRecord(debit,credit,describe,article,operation)
            else:
                st.warning("عملية متوازتة")
