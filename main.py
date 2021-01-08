from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    return "success", 200

@app.route('/register/', methods=['GET', 'POST'])
def register():
    return "success", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
