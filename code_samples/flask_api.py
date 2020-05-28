#!flask/bin/python
from flask import Flask, jsonify
from flask_cors import CORS #per https://flask-cors.readthedocs.io/en/latest/

api = Flask(__name__)
CORS(api) # per https://flask-cors.readthedocs.io/en/latest/

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@api.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    api.run(debug=True,host='0.0.0.0', port=5001)
