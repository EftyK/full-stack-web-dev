#!/bin/python

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import random
import math
import json



app = Flask(__name__)


# Configure SQLAlchemy to use an SQLite in-memory database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple.db'
# db = SQLAlchemy(app)


# # Define your database model
# class DatabaseModel(db.Model):
#     __tablename__ = 'locations'
#     id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(100))
    # Add other columns as per your existing table structure



# Route to display contents of the SQLite database
@app.route('/show_data')
# def show_data():
#     # Fetch data from the database
#     data = DatabaseModel.query.all()  # Retrieve all data from the table

#     return render_template('show_data.html', data=data)

# @app.route('/')
def display_data():
    # Establish a connection to the database
    conn = sqlite3.connect('simple.db')
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT * FROM locations")
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    return render_template('show_data.html', data=data)

# If you're not going to modify the schema, set this to False to suppress the warning
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def randomPoint(): # create random point 0 - 100
	return random.randint(1,100), random.randint(1,100)

def euclidean_distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


@app.route("/")
def index():
	x1, y1 = randomPoint()
	x2, y2 = randomPoint()
	dist = euclidean_distance(x1, y1, x2, y2)
	return render_template("index.html", point1=(x1,y1), point2=(x2,y2), distance=dist)

# app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)