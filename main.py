
# main.py

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phase = db.Column(db.Integer)
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))

    def __repr__(self):
        return '<Task %r>' % self.name

@app.route('/')
def index():
    phases = db.session.query(Task).distinct(Task.phase).all()
    return render_template('index.html', phases=phases)

@app.route('/phase/<int:phase_number>')
def phase(phase_number):
    tasks = db.session.query(Task).filter_by(phase=phase_number).all()
    return render_template('phase.html', phase_number=phase_number, tasks=tasks)

@app.route('/phase/<int:phase_number>/add_task', methods=['GET', 'POST'])
def add_task(phase_number):
    if request.method == 'POST':
        task = Task(phase=phase_number, name=request.form['name'], description=request.form['description'])
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('phase', phase_number=phase_number))
    return render_template('add_task.html', phase_number=phase_number)

@app.route('/phase/<int:phase_number>/delete_task/<int:task_id>')
def delete_task(phase_number, task_id):
    task = db.session.query(Task).filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('phase', phase_number=phase_number))

@app.route('/phase/<int:phase_number>/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(phase_number, task_id):
    task = db.session.query(Task).filter_by(id=task_id).first()
    if request.method == 'POST':
        task.name = request.form['name']
        task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('phase', phase_number=phase_number))
    return render_template('edit_task.html', phase_number=phase_number, task=task)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
