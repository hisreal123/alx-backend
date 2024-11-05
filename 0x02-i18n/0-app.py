#!/usr/bin/env python3
""" A simple flask app"""


from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
  """ a single route"""
  return render_template('0-index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5000', debug=True)
