import pymysql
from sqlalchemy import create_engine
import pandas as pd
from flask import Flask
import json

#Frail Region
#Spørgsmål 1 mangler, da jeg ikke kan finde test.sql

con= pymysql.connect(host="localhost", user="root", password="", db="pyw8")
engine = create_engine('mysql+pymysql://root:@localhost/pyw8')
name = "statskode"
def import_data():
    data = pd.read_csv("befkbhalderstatkode.csv")
    data.to_sql(name, engine, if_exists='replace', index=False)

def get_data():
    sql_query = f'SELECT * FROM {name}'
    data = None
    with con.cursor() as cursor:
        cursor.execute(sql_query)
        data = cursor.fetchall()
    return data

app = Flask(__name__)
@app.route("/")
def index():
    return json.dumps(get_data())

if __name__ == "__main__":
    app.run(debug=True)
