"""
Author: Kelv Gooding
Created: 2024-01-01
Updated: 2025-03-11
Version: 1.2
"""

# Modules

from flask import Flask, render_template, request, flash
import os
import mysql.connector
from modules import db_check
from modules import config

# MariaDB Variables

conn = mysql.connector.connect(
    host=config.DB_HOST,
    port='3306',
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database='sample-app'
)

# SQLite3 Variables

# db_filename = 'user_input_form.db'
# base_path = os.path.dirname(os.path.abspath(__file__))
# sql_script = f'{base_path}/scripts/sql/create_tables.sql'
# db_check.check_db(f'{base_path}', f'{db_filename}', f'{sql_script}')
# conn = db_check.sqlite3.connect(os.path.join(base_path, db_filename), check_same_thread=False)

c = conn.cursor()

# Flask Variables

app = Flask(__name__)
app.secret_key = os.urandom(26)

# General Variables

filename = 'locations.txt'
list_of_counties = []

@app.route("/")
def index():

    with open(filename, "r") as file:
        for i in file:
            list_of_counties.append(i.strip())

    return render_template("index.html", list_of_counties=list_of_counties)

@app.route("/", methods=["POST"])
def customers():

    if request.method == "POST":
        c.execute('INSERT INTO user (first_name, last_name, age, location) VALUES (%s, %s, %s, %s)', (request.form.get("first_name"), request.form.get("last_name"), request.form.get("age"), request.form.get("location")))
        conn.commit()

        flash("A new entry has now been added!")
        return render_template("index.html", list_of_counties=list_of_counties)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)