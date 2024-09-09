import streamlit as st
from objs.database import Database

with st.form('add_db'):
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    host = st.text_input('Host')
    port = st.text_input('Port')
    db_name = st.text_input('Database Name')

    db_system = st.selectbox('Database System', ['PostgreSQL', 'MySQL', 'SQLite'])
    submit = st.form_submit_button('Add Database')

    if submit:
        new_db = Database()
        new_db.add_new_config(username, password, host, port, db_name, db_system)
        submit = False


