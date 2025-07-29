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