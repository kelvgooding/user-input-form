# Modules

from flask import Flask, render_template, request, flash
import sqlite3
import os

# Flask Variables

app = Flask(__name__)
app.secret_key = os.urandom(26)

# SQLite3 Variables

connection = sqlite3.connect('user_input_form.db', check_same_thread=False)
cursor = connection.cursor()

# Script

@app.route("/")
def index():

    towns = []

    cursor.execute("SELECT * FROM towns;")

    for i in cursor.fetchall():
        towns.append(i[0])

    return render_template("index.html", towns=towns)

@app.route("/", methods=["POST"])
def customers():

    if request.method == "POST":
        cursor.execute('INSERT INTO user VALUES (?, ?, ?, ?)', (request.form.get("first_name"), request.form.get("last_name"), request.form.get("age"), request.form.get("location"),))
        connection.commit()

        flash("A new entry has now been added!")
        return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)