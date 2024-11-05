from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_babel import Babel

app = Flask(__name__, static_folder='static', template_folder='templates')
# app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
CORS(app)

class Config:
    LANGUAGES = ['en', 'us']

@app.route('/')
def index():
  return render_template('0-index.html')


if __name__ == '__main__':
  app.run(debug=True)
