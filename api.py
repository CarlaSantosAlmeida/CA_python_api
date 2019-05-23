# Flask API
from typing import Optional, Any

from flask import Flask, jsonify
from flask_cors import CORS
import dataset
import datetime
import random

app = Flask(__name__)

@app.route('/')
def send_default():
    return "Hello World!"

@app.route('/get')
def send_get():
    db = dataset.connect('sqlite:///api.db')
    table = db['random_data']
    now = datetime.datetime.now()
    luck = random.gauss(22, 4)
    data = {'time': now, 'value': luck}
    table.insert(data)

    data = table.all()  # traz tudo da BD
    return jsonify([x for x in data])

if __name__ == '__main__':
    app.run()