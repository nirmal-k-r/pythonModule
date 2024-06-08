from flask_sqlalchemy import SQLAlchemy

#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'example.db')

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(256))
    done = db.Column(db.Boolean)

def add_task(id, title, description,done):
    new_task = Task(id, title=title, description=description, done=False)
    db.session.add(new_task)
    db.session.commit()


# def __repr__(self):
#     return (f'<Task {self.title}> : {self.description} : {self.done}')


# def __str__(self):
#     return (f'<Task {self.title}> : {self.description} : {self.done}')