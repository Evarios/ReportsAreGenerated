sql_prompt_template = """
### Task
Generate a SQL query for {dbms} to answer [QUESTION]{question}[/QUESTION]

### Instructions
- If you are not sure about the answer with the available database schema, return 'I do not know'.
- Before You return the query, make sure that all tables are initialized.
- As an answer, return only the code.

### Database Schema
The query will run on a database with the following schema:
{schema}


### Answer
Given the database schema, here is the SQL query that answers [QUESTION]{question}[/QUESTION]
"""

code_template = """
import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


load_dotenv('existing/{database}/.env', override=True, verbose=True)

USERNAME = os.getenv('PGUSERNAME')
PASSWORD = os.getenv('PGPASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('NAME').replace('"', '')
URL = f'{url}'

engine = create_engine(URL)

df = pd.read_sql("{query}", engine)

{code}
"""

code_prompt_template = """
### Task
Assume You are expirieced data visualisation engineer.
Write a Python code which will handle following question: [QUESTION]{question}[/QUESTION]

### Instructions
- Before You return the code, make sure that all variables are defined and you are using the correct columns and datatypes.
- Use only matplotlib for plotting,
- Always use plt.tight_layout() after plotting to ensure that the plot is not cut off.
- Always save the plot as 'plot.png' in the current directory.
- Always add legend to the plot.
- Don't show plot in the end.
- 
- You must finish following code:
```python
import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

load_dotenv()

USERNAME = os.getenv('PGUSERNAME')
PASSWORD = os.getenv('PGPASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')
URL = f'{url}'

engine = create_engine(URL)

df = pd.read_sql('{query}', engine)

# Finish your code here
```
- Don't change anything in the code above.
- Return ONLY code!

### Answer
Here is the Python code that answers [QUESTION]{question}[/QUESTION]

Begin!
"""