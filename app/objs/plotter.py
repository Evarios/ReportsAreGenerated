import os
import subprocess
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from prompts import sql_prompt_template, code_prompt_template, code_template


class Plotter:
    def __init__(self):
        self.sql_llm = ChatOllama(model='sqlcoder:7b')
        self.sql_prompt = PromptTemplate.from_template(sql_prompt_template)
        self.sql_chain = self.sql_prompt | self.sql_llm

        self.code_llm = ChatOllama(model='Niro/mistral-7b-python:latest')
        self.code_prompt = PromptTemplate.from_template(code_prompt_template)
        self.code_chain = self.code_prompt | self.code_llm


    # ========================= PUBLIC METHODS ========================= #
    def generate_sql_query(self, question: str, database: str) -> str:

        schema = self._fetch_metadata(f'existing/{database}/metadata.sql')

        sql_query = self.sql_chain.invoke({
            'question': question,
            'schema': schema,
        }).content

        return sql_query.strip().replace('<s> ', '')
    
    def generate_code(self, question: str, sql_query: str) -> str:
        code = self.code_chain.invoke({
            'question': question,
            'query': sql_query,
        }).content

        return code.replace('```python\n', '').replace('```', '')
    
    def execute_code(self, file_path: str, code_template: str, sql_query: str, code: str) -> None:

        code_template = code_template.format(
            query=sql_query,
            code=code
        )

        with open(file_path, 'w') as f:
            f.write(code_template)

        result = subprocess.run(['python', file_path], stderr=subprocess.PIPE)
        os.remove(file_path)

        print(result.stderr.decode('windows-1252'))

        return result.stderr.decode('windows-1252'), len(result.stderr.decode('windows-1252'))

    
    # ========================= PRIVATE METHODS ========================= #

    def _fetch_metadata(self, file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.read()

    