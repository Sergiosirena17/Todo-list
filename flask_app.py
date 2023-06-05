from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return render_template('index.html', tasks=tasks)

    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:index>', methods=['GET'])
def delete_task(index):
    del tasks[index]
    return render_template('index.html', tasks=tasks)

@app.route('/mark-all', methods=['POST'])
def mark_all():
    checked = request.form.getlist('checkbox')

    for i in range(len(tasks)):
        if str(i) not in checked:
            tasks[i] = '<|||>' + tasks[i] + '<|||>'
    
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run()
