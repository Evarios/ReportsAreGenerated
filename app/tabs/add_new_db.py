import streamlit as st
from objs.database import Database

def add_new_db():

    server_instance = None
    how_to_connect = None
    host = None
    port = None

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    db_system = st.selectbox('Database System', ['Oracle', 'PostgreSQL', 'MySQL', 'Microsoft SQL Server', 'MongoDB'])

    # MS SQL form
    if db_system == 'Microsoft SQL Server':
        server_instance = st.text_input('Server Instance')
        db_name = st.text_input('Database Name')

    # Oracle form
    elif db_system == 'Oracle':
        host = st.text_input('Host')
        port = st.text_input('Port')
        how_to_connect = st.radio('How to connect?', ['SID', 'SERVICE_NAME'])
        db_name = st.text_input(how_to_connect)

    # PostgreSQL,MySQL and MongoDB form
    else:
        host = st.text_input('Host')
        port = st.text_input('Port')
        db_name = st.text_input('Database Name')

    with st.form('add_db'):
        submit = st.form_submit_button('Add Database')

        if submit:
            if db_system == 'Oracle':
                db_system = f'{db_system}_{how_to_connect}'

            new_db = Database()
            if server_instance:
                new_db.add_new_config(username, password, host, port, db_name, db_system, server_instance)
            else:
                new_db.add_new_config(username, password, host, port, db_name, db_system)

            submit = False
            st.success('Database added successfully!')