#!/usr/bin/env python3
""" A simple flask app"""


from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def index():
  """ a single route"""
  return render_template('0-index.html')


if __name__ == '__main__':
  app.run(debug=True)
