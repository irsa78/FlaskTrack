from flask import Flask, render_template, request
import requests


import sqlite3
number="+447878066443"


# . . .
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn




if __name__ == "__main__":
	app.run(debug=True)