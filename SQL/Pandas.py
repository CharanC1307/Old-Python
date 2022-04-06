import pandas as pd
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=CHARANPC\SQLEXPRESS;'
                      'Database=Student;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

sql_query = pd.read_sql_query('SELECT * FROM dbo.students',conn)
print(sql_query)
print(type(sql_query))