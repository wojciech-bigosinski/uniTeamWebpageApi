from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

users = [
    {"id": '1', "username": 'admin', "password": 'admin', "firstName": 'Admin', "lastName": 'User', "role": "Admin"},
    {'id': '2', "username": 'user', "password": 'user', "firstName": 'Normal', "lastName": 'User', "role": "User"},
    {'id': '3', "username": 'fc', "password": 'fc', "firstName": 'Fc', "lastName": 'User', "role": "FC"}
]

polls = []

rewards = [
    {"id": "1", "name": "reward1", "description": "description", "cost": "100"},
    {"id": "2", "name": "reward2", "description": "description", "cost": "200"},
    {"id": "3", "name": "reward3", "description": "description", "cost": "300"}
]

@app.route('/login/', methods=['GET', 'POST'])
def login():
    data = request.json
    for user in users:
        if user.get("username") == data.get("username") and user.get("password") == data.get("password"):
            return jsonify(user), 200
    return "unsuccessful", 200

@app.route('/register/', methods=['GET', 'POST'])
def register():
    data = request.json
    users.append(data)
    return "success", 200

@app.route('/poll/', methods=['GET', 'POST'])
def commitPoll():
    data = request.json
    polls.append(data)
    return "success", 200

@app.route('/changeUser/', methods=['GET', 'POST'])
def changeUser():
    return "success", 200

@app.route('/banUser/', methods=['GET', 'POST'])
def banUser():
    data = request.json
    for user in users:
        if user.get("username") == data.get("username"):
            users.remove(user)
    return "success", 200

@app.route('/changeReward/', methods=['GET', 'POST'])
def changeReward():
    return "success", 200

@app.route('/addReward/', methods=['GET', 'POST'])
def addReward():
    return "success", 200

@app.route('/deleteReward/', methods=['GET', 'POST'])
def deleteReward():
    data = request.json
    for reward in rewards:
        if reward.get("name") == data.get("name"):
            rewards.remove(reward)
    return "success", 200

@app.route('/claimReward/', methods=['GET', 'POST'])
def claimReward():
    return "success", 200

if __name__ == '__main__':
    app.run(host='localhost', port=105)
