import streamlit as st
from tabs.chat import chat
from tabs.add_new_db import add_new_db

# Tytuł aplikacji
st.title("Generate plots!")

# Tworzenie zakładek
chat_tab, db_tab = st.tabs(["Chat", "Add new database"])

# Treść dla zakładki 1
with chat_tab:
    chat()

# Treść dla zakładki 2
with db_tab:
    add_new_db()
