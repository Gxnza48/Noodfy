from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    
]

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/tasks')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    if task_text:
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "text": task_text, "done": False})
    return redirect(url_for('index'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['done'] = not task['done']
            break
    return '', 204

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
