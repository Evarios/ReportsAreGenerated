from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.agents import tool, create_react_agent, AgentExecutor

from prompts import sql_prompt, react_prompt, code_prompt

def load_txt(path: str):
    with open(path, 'r') as f:
        return f.read()
    
SQL_LLM = ChatOllama(model='sqlcoder:7b')
CODE_LLM = ChatOllama(model='Niro/mistral-7b-python:latest')
LLM = ChatOllama(model='mistral')



@tool
def create_query(query):
    """Function takes Question as an input and returnes an sql query based on the question. Don't pass the query as a parameter, it will be returned."""
    template = PromptTemplate.from_template(sql_prompt)
    chain = template | SQL_LLM
    return chain.invoke(input={'constraints': load_txt('constraints.txt'), 'tables': load_txt('tables.txt'), 'query': query}).content

@tool 
def create_code(question):
    """Funtion takes question and SQL query as an input and returns a python code based on the input question and query."""
    template = PromptTemplate.from_template(code_prompt)
    chain = template | CODE_LLM
    return chain.invoke(input={'question': question}).content



if __name__ == '__main__':

    query = "Draw pie chart of number of films in each category?"

    tools = [create_query,
             create_code]

    prompt = PromptTemplate.from_template(react_prompt)

    agent = create_react_agent(prompt=prompt, llm=LLM, tools=tools)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    result = agent_executor.invoke(
        input={'input': query},
    )

    print(result['output'])