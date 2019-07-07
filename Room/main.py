from flask import Flask, jsonify, request
from django.http import HttpResponse
from hue import Hue

hue = Hue()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return "Welcome to Hue", 200

@app.route('/all/on', methods = ['GET'])
def all_on():
    hue.all_on(.2)
    return "All lights now on", 200


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)
