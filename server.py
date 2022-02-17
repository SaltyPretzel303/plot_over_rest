from http.client import HTTPResponse
from io import BytesIO, StringIO

from turtle import color
from flask import Flask, request, jsonify, send_file
from flask_restful import Resource, Api
import json

import matplotlib.pyplot as plt

points = []


class Point():
    def __init__(self, x_value, y_value, color):
        self.x = x_value
        self.y = y_value
        self.color = color

    def print(self):
        print("x: "+str(self.x)+" y: "+str(self.y))


app = Flask(__name__)
api = Api(app)


@app.route('/add', methods=['POST'])
def addPoint():
    data = json.loads(request.data)
    print(data)
    points.append(Point(data['x'], data['y'], 'unknown'))

    return '200'


@app.route('/print', methods=['GET'])
def printPoints():

    x_points = []
    y_points = []
    for point in points:
        point.print()

        x_points.append(point.x)
        y_points.append(point.y)

    plt.plot(x_points, y_points)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png')


@app.route('/clear', methods=['GET'])
def clearPoints():
    points.clear()

    return '200'


if __name__ == '__main__':
    app.run(port='8000')
