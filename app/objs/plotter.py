import os
import subprocess
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from prompts import sql_prompt_template, code_prompt_template, code_template

load_dotenv()

class Plotter:
    def __init__(self):

        self.model = ChatOpenAI(model='gpt-3.5-turbo', api_key=os.getenv('OPENAI_API_KEY'))
                                        
        self.sql_prompt = PromptTemplate.from_template(sql_prompt_template)
        self.sql_chain = self.sql_prompt | self.model
            
        self.code_prompt = PromptTemplate.from_template(code_prompt_template)
        self.code_chain = self.code_prompt | self.model


    # ========================= PUBLIC METHODS ========================= #
    def generate_sql_query(self, question: str, database: str) -> str:

        schema = self._fetch_metadata(f'existing/{database}/metadata.sql')

        sql_query = self.sql_chain.invoke({
            'question': question,
            'schema': schema,
        })

        return sql_query.content
    
    def generate_code(self, question: str, sql_query: str) -> str:
        code = self.code_chain.invoke({
            'question': question,
            'query': sql_query.replace('```sql', '').replace('```', '').replace('\n', ' '),
        })

        return code.content
    
    def execute_code(self, file_path: str, code_template: str, sql_query: str, code: str) -> None:

        code_template = code_template.format(
            query=sql_query.replace('```sql', '').replace('```', '').replace('\n', ' '),
            code=code.replace('```python', '').replace('```', '')
        )

        print(code_template)

        with open(file_path, 'w') as f:
            f.write(code_template)

        result = subprocess.run(['python', file_path], stderr=subprocess.PIPE)
        os.remove(file_path)

        print(result.stderr.decode('windows-1252'))

        return result.stderr, len(result.stderr)

    
    # ========================= PRIVATE METHODS ========================= #

    def _fetch_metadata(self, file_path: str) -> str:
        with open(file_path, 'r') as f:
            return f.read()

    