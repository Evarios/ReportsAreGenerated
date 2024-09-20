import streamlit as st
from objs.database import Database

def add_new_db():

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    host = st.text_input('Host')
    port = st.text_input('Port')
    db_system = st.selectbox('Database System', ['Oracle', 'PostgreSQL', 'MySQL'])

    if db_system == 'Oracle':
        how_to_connect = st.radio('How to connect?', ['SID', 'SERVICE_NAME'])
        db_name = st.text_input(how_to_connect)
    else:
        db_name = st.text_input('Database Name')

    with st.form('add_db'):
        submit = st.form_submit_button('Add Database')

        if submit:
            if db_system == 'Oracle':
                db_system = f'{db_system}_{how_to_connect}'
            new_db = Database()
            new_db.add_new_config(username, password, host, port, db_name, db_system)
            submit = False
            st.success('Database added successfully!')