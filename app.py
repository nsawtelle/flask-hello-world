from flask import Flask
import psycopg
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Nicole Sawtelle in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg.connect("postgresql://db_3308_flask_db_user:80XZPI6NZDC7TVZa2OifsiV6yTm8cEAR@dpg-d23rademcj7s739m9jag-a/db_3308_flask_db")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg.connect("postgresql://db_3308_flask_db_user:80XZPI6NZDC7TVZa2OifsiV6yTm8cEAR@dpg-d23rademcj7s739m9jag-a/db_3308_flask_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball table created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg.connect("postgresql://db_3308_flask_db_user:80XZPI6NZDC7TVZa2OifsiV6yTm8cEAR@dpg-d23rademcj7s739m9jag-a/db_3308_flask_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Nicole', 'Sawtelle', 'CU Boulder', 'Team 4', 3308);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg.connect("postgresql://db_3308_flask_db_user:80XZPI6NZDC7TVZa2OifsiV6yTm8cEAR@dpg-d23rademcj7s739m9jag-a/db_3308_flask_db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basketball;")
    records = cur.fetchall()
    conn.close()
    
    response = "<table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
    for row in records:
        response += "<tr>" + "".join([f"<td>{cell}</td>" for cell in row]) + "</tr>"
    response += "</table>"
    return response
    
@app.route('/db_drop')
def db_drop():
    conn = psycopg.connect("postgresql://db_3308_flask_db_user:80XZPI6NZDC7TVZa2OifsiV6yTm8cEAR@dpg-d23rademcj7s739m9jag-a/db_3308_flask_db")
    cur = conn.cursor()
    cur.execute("DROP TABLE Basketball;")
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"