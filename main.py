from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import subprocess
import os

from app.static.prompts import sql_prompt_template, code_prompt_template, code_template

def load_metadata(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()
    
def save_code(file_path: str, code_template: str, sql_query: str, code: str) -> None:

    code_template = code_template.format(
        query=sql_query,
        code=code
    )

    with open(file_path, 'w') as f:
        f.write(code_template)


SQL_LLM = ChatOllama(model='sqlcoder:7b')
CODE_LLM = ChatOllama(model='Niro/mistral-7b-python:latest')

QUESTION = 'Draw pie chart of number of films in each language.'


if __name__ == '__main__':
    
    schema = load_metadata('metadata/metadata.sql')

    # ========================= SQL Query Generation =========================
    sql_prompt = PromptTemplate.from_template(sql_prompt_template)

    sql_chain = sql_prompt | SQL_LLM

    sql_query = sql_chain.invoke({
        'question': QUESTION,
        'schema': schema,
    }).content

    sql_query = sql_query.strip().replace('<s> ', '')

    # ========================= Code Generation =========================

    code_prompt = PromptTemplate.from_template(code_prompt_template)

    code_chain = code_prompt | CODE_LLM

    code = code_chain.invoke({
        'question': QUESTION,
        'query': sql_query,
    }).content


    # ========================= Save Code =========================

    save_code('plot.py', code_template, sql_query, code)

    # ========================= Execute Code =========================

    subprocess.run(['python', 'plot.py'])
    os.remove('plot.py')

