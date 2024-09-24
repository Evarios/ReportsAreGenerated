# ReportsAreGenerated

Aim of this project is to build a system capable to connect to any database and draw a figure based on the prompt.

## How to run project:
1. Install necesarry frameworks: `pip install -r requirements.txt`,
2. Go to *app* directory: `cd app`,
3. Run streamlit app: `streamlit run app.py`,
4. Create `.env` file and add there Your `OPENAI_API_KEY`.

## Contents:

1. [Adding database connection,](#db)
    * [Oracle SQL Server,](#oracle)
    * [Microsoft SQL Server,](#MSQL)
    * [PostgreSQL, MySQL,](#postgres)
2. [Generating figures.](#gen)

<a name="db"></a>

## 1. Adding database connection. 

At the very beginning You'll see layout like below:

![image](https://github.com/user-attachments/assets/61cac8b0-be04-488a-a86b-c38f7fa8d10e)

Reason of this is that You haven't added any database connection yet. To do this, go to ***Add new database*** tab. After that You'll see a form which You have to complete with appropriate data. General shape of form may be diffrent for each DBMS. It is caused of the diffrent ways to connect with this systems. After clicking button ***Add database*** app will create new directory in `existing/`, then creates `.env` file which contains all db connection details.

<a name="oracle"></a>

### Oracle SQL Server.

Form to add Oracle DB connection looks like below:

![image](https://github.com/user-attachments/assets/b652b386-23f5-44d2-b73f-0b1c25a280d9)

To propertly run configuration You have to add <a href="https://www.oracle.com/pl/database/technologies/sqlplus-cloud.html">*sqlplus*</a> to global PATH variables. Form allows You to connect with database by SID and Service Name.

<a name="MSQL"></a>

### Microsoft SQL Server.

![image](https://github.com/user-attachments/assets/e23fbcef-ef1c-4e11-96f8-d9845e5fa830)

First of all, You have to download <a href="https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16">ODBC Driver</a>. Except that you have to download extension for SQL Server:

```
Install-Module -Name SqlServer`
```

<a name="postgres"></a>

### PostgreSQL, MySQL.

![image](https://github.com/user-attachments/assets/19c1c0bd-8506-463d-bd77-29ef098d2af0)

Form for both DBMSs are the same. If You're using PostgreSQL add `pg_dump` to global PATH variables. Otherwise add `mysqkdump` to PATH global variables.

To show an example I'll use <a href="https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/">dvdrental</a> sample database. Making connection showed below:

![image](https://github.com/user-attachments/assets/bd609245-23ab-4d02-abcd-948587f705ee)

<a name="gen"></a>

## 2. Generating figures.

Go back to *Chat* tab and refresh the page. Now You should see available connections:

![image](https://github.com/user-attachments/assets/a13d08e8-ffd3-45cc-9d8a-b6eedefa7a30)

Now in text field You have to provide sentence what plot You want to see. In my example I'm gonna plot a pie chart of amount of films in each category. Results showed below:

![image](https://github.com/user-attachments/assets/369d65e1-3cc6-4cd9-9061-d2b54e01f953)


