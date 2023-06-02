import sqlite3
import pandas as pd
import itertools
con=sqlite3.connect('C:\\Users\\acm\\Desktop\\questionwebsite\\website\\mysite\\questionpaper9.db')
cursor = con.cursor()
sql=f"SELECT * FROM ioecropedquestionpaper where desc like '%candidate%' "
object=cursor.execute(sql)

import itertools

val = object.description
column_names = [col[0] for col in val]
data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
print(data)

