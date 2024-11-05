from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/data', methods=['GET'])
def get_data():
  return jsonify({'message': 'Home from flask !'})

if __name__ == '___main__' 