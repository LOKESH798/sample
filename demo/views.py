from django.shortcuts import render
import pandas as pd 
import psycopg2
# conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
# cur = conn.cursor()
from sqlalchemy import create_engine

def index(request):
    
  
    #   with open('user_accounts.csv', 'r') as f:
    # # Notice that we don't need the `csv` module.
    #         next(f) # Skip the header row.
    #         cur.copy_from(f, 'users', sep=',')

    #   conn.commit()
    #    #data = pd.read_csv("nba.csv") 
    #   for col in data.columns:
    #         dataTypeSeries = data.dtypes[col]
    #         print(dataTypeSeries)
      return  render(request,"index.html")

def save(request):

      ur=request.POST.get('url')
      l="C:/Users/logesh/Desktop/"+ur
      print(l)
      df = pd.read_csv (l) 
        
      df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces


      engine = create_engine('postgresql://postgres:1234@localhost:5432/sample')

      df.to_sql("sales_engine", engine)
     

      return render(request,"index.html")