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

@app.route('/poll/', methods=['GET', 'POST'])
def commitPoll():
    return "success", 200

@app.route('/changeUser/', methods=['GET', 'POST'])
def changeUser():
    return "success", 200

@app.route('/banUser/', methods=['GET', 'POST'])
def banUser():
    return "success", 200

@app.route('/changeReward/', methods=['GET', 'POST'])
def changeReward():
    return "success", 200

@app.route('/addReward/', methods=['GET', 'POST'])
def addReward():
    return "success", 200

@app.route('/deleteReward/', methods=['GET', 'POST'])
def deleteReward():
    return "success", 200

@app.route('/claimReward/', methods=['GET', 'POST'])
def claimReward():
    return "success", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
