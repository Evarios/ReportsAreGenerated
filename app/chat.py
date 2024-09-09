import streamlit as st
from objs.plotter import Plotter
from objs.database import Database

from prompts import code_template

database = Database()
plotter = Plotter()

database = st.selectbox('Choose a database which you want to work with', database.get_added_databases())

with st.form('genAI'):
    query = st.text_area('What do You want to plot?')
    submit = st.form_submit_button('Generate plot!')

    if submit:
        st.write('Fetching data from database...')
        sql_query = plotter.generate_sql_query(query, database)
        st.write(sql_query)
        st.write('Generating plot...')
        status = 1
        while status:
            code = plotter.generate_code(query, sql_query)
            message, status = plotter.execute_code('plot.py', code_template, sql_query, code)
            if status:
                code_returned = code_template.format(
                    query=sql_query,
                    code=code
                )
                query = """
                My code is:
                {code}
                I got an error: 
                {message}
                Fix it to answer my question:
                {query}
                """.format(code=code_returned, message=message, query=query)
                st.write("I found some bugs in my code and I'm trying to fix them. Please wait...")

        st.image('plot.png')
        submit = False