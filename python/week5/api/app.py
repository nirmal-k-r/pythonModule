from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Task import Task

#create server
app = Flask(__name__)

#configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
from models.Task import db
db.init_app(app)

with app.app_context():
    #initialise database
    db.create_all()
    tasks = [
    {'id': 1, 'title': 'Do homework', 'description': 'Math, Physics', 'done': False},
    {'id': 2, 'title': 'Read book', 'description': 'Fiction', 'done': False}
    ]
    for task in tasks:
        new_task=Task(title=task['title'], description=task['description'], done=task['done'])
        db.session.add(new_task)
        db.session.commit()


#routes
#get-route
@app.route('/', methods=['GET'])
def index():
    return jsonify({'api': 'works'})
                   
#get-route
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks=Task.query.all()
    to_return=[(f'<Task {task.title}> : {task.description} : {task.done}') for task in tasks]
    return ({'tasks': to_return})
    
#add route
@app.route('/add', methods=['POST'])
def add_tasks():
    task=request.json
    new_task=Task(task['id'],task['title'], task['description'], task['done'])
    db.session.add(new_task)
    db.session.commit()
   

if __name__ == '__main__':
   app.run(port=3000)  
