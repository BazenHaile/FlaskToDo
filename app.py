from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

todos = []

@app.route('/')
@app.route('/home')  # Make sure to include the root route to default to home
def home():
    # Pass the todos list to the home.html template
    return render_template('home.html', todos=todos)

@app.route('/manage')  # Route for 'manage'
def manage():
    # Pass the todos list to the manage.html template
    return render_template('manage.html', todos=todos)

@app.route('/contact')  # Route for 'contact'
def contact():
    # Renders 'contact.html'
    return render_template('contact.html')

@app.route('/about')  # Route for 'about'
def about():
    # Renders 'about.html'
    return render_template('about.html')

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, 'done': False})
    # Redirect to the manage page to see the updated list
    return redirect(url_for('manage'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        todo = request.form['todo']
        todos[index]['task'] = todo
        # Redirect to the manage page to see the changes
        return redirect(url_for('manage'))
    else:
        # Render the edit template with the todo item and its index
        return render_template('edit.html', todo=todos[index], index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    # Redirect to the manage page to immediately see the toggled status
    return redirect(url_for('manage'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    # Redirect to the manage page to see the list after deletion
    return redirect(url_for('manage'))

if __name__ == '__main__':
    app.run(debug=False)
