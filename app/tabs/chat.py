import streamlit as st
from objs.plotter import Plotter
from objs.database import Database

from prompts import code_template


def chat():
    if 'plotter' not in st.session_state:
        st.session_state['plotter'] = Plotter()

    if 'database' not in st.session_state:
        st.session_state['database'] = Database()

    database = st.selectbox('Choose a database which you want to work with', st.session_state['database'].get_added_databases())

    with st.form('genAI'):
        query = st.text_area('What do You want to plot?')
        submit = st.form_submit_button('Generate plot!')

        if submit:
            st.write('Fetching data from database...')
            sql_query = st.session_state['plotter'].generate_sql_query(query, database)
            st.write(sql_query)
            if sql_query != 'I do not know.':
                st.write('Generating plot...')
                code = st.session_state['plotter'].generate_code(query, sql_query)
                st.write(code)
                message, status = st.session_state['plotter'].execute_code('plot.py', code_template, sql_query, code, database)
                st.image('plot.png')
                submit = False