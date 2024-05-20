#!/usr/bin/python3
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('states.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/states_list')
def states_list():
    conn = get_db_connection()
    states = conn.execute('SELECT * FROM states').fetchall()
    conn.close()
    return render_template('states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
