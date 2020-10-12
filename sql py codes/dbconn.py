import pyodbc
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=LAPTOP-GJOUEUG9;'
                      'Database=stu;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT *FROM fun.dbo.emp1')

for row in cursor:
    print(row)

  

   