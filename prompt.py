prompt = """
Write a query in for postgreSQL which will handle the question.
Return only the SQL code.
Constraints:
{constraints}
Tables and columns:
{tables}
Question: {query}
"""