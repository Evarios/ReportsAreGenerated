from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

from prompt import prompt

def load_constraints(path: str):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    llm = ChatOllama(model='sqlcoder:7b')

    template = PromptTemplate.from_template(prompt)
    query = "Show all the actors first and last name who have acted in more than 5 movies and amount of movies in which they played."

    chain = template | llm

    result = chain.invoke(input={'constraints': load_constraints('constraints.txt'), 'tables': load_constraints('tables.txt'), 'query': query})
    print(result.content)