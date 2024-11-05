from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__, static_folder='static', template_folder=)
CORS(app)


@app.route('/api/data', methods=['GET'])
def get_data():
  return jsonify({'message': 'Home from flask !'})

if __name__ == '__main__':
  app.run(debug=True)
  