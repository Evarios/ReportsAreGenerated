import os
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

sql_prompt = """
Based on constraints, tables and columns write a query in for postgreSQL which will handle the question: {query}
Return only the SQL code.
Constraints:
{constraints}
Tables and columns:
{tables}
"""

code_prompt = """
Write a code in python which will handle the question: {question}
Always use plt.tight_layout() and save plot as 'plot.png'.
Return code in following format:

```python
from dotenv import load_dotenv
import pandas as pd
import os
from sqlalchemy import create_engine

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
host = os.getenv('HOST')
port = os.getenv('PORT')
url = f'postgresql://{{username}}:{{password}}@{{host}}:{{port}}/{{database}}'

engine = create_engine(url)

data = pd.read_sql({{here is place for query}}, engine)
# Your code creating plot here
```
"""

react_prompt = """
You are programist and you have to write a code in python which will handle the question.
After you use a tool, finish.
You must use the following tools:

{tools}

Use the following format:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer must be the code that's returned.

Begin!

Question: {input}

Thought:{agent_scratchpad}
"""