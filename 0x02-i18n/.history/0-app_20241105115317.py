from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)


@app.route('/')
def index():
  return render_template('0-')

if __name__ == '__main__':
  app.run(debug=True)
  