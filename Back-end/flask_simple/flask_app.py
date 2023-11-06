#!/bin/python

from flask import Flask, render_template
import random
import math
import json



app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)