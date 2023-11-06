#!/bin/python

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json



app = Flask(__name__)


# Route to display contents of the SQLite database
@app.route('/show_data')
def show_data():
    # Establish a connection to the database
    conn = sqlite3.connect('simple.db')
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT * FROM locations")
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    return jsonify({'locations': data})



@app.route('/save_location', methods=['POST'])
def save_entry():
    data = request.get_json()
    print(data)
    name = data.get('name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Establish a connection to the database file
    conn = sqlite3.connect('simple.db')
    cursor = conn.cursor()

    # Execute an INSERT query to add data to the SQLite database
    cursor.execute("INSERT INTO locations (name, latitude, longitude) VALUES (?, ?, ?)", (name, latitude, longitude))

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

    return jsonify({'message': 'Data saved successfully'})


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)