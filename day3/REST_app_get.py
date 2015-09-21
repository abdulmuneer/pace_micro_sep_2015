from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Learn Python',
        'description': u'import this', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn REST',
        'description': u'Need to learn REST to setup APIs for automation framework', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
