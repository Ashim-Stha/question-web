from django.shortcuts import render ,HttpResponse
from django import forms
import sqlite3
import pandas as pd
import itertools
con=sqlite3.connect('C:\\Users\\ashim\\OneDrive\\Desktop\\land\\questionwebsite\\website\\mysite\\questionpaper9.db',check_same_thread=False)
cursor = con.cursor()
# Create your views here.
def index(request):
  
    return render(request,'index.html')
    
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q') # Pass request.GET to bind the form data
        if query == '':
            return render(request,'index.html')
        url="https://github.com/prathamadh/photobase/blob/3b07f326fb0ec6346694076434b63649e4b20a33/"
        sql=f"SELECT * FROM ioecropedquestionpaper where desc like '%{query}%' "
        object=cursor.execute(sql)
        val = object.description
        column_names = [col[0] for col in val]
        data = [dict(zip(column_names, row))  
            for row in cursor.fetchall()]
       
        return render(request, 'search_results.html', {'query': query,'results':data,'url':url})
       

