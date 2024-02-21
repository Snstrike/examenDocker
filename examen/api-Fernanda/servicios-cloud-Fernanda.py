from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configurar la conexión a MongoDB
client = MongoClient('mongodb://mongodb-service.bd-fernanda:27017/') #change to full name
db = client['mydatabase']
collection = db['users']

@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    collection.insert_one({'name': name})
    return jsonify({'message': 'Usuario agregado'}), 201

@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    for user in collection.find():
        users.append(user['name'])
    return jsonify({'users': users}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
