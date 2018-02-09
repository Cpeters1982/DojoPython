from flask import Flask, render_template, redirect, request, session
'''
This simple app counts the numbe rof times index.html has been loaded by the user in session. 
Demonstrates session, persistent data and POST routes
'''
app = Flask(__name__)
app.secret_key = "KeepItSecret"

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 0
    return render_template('index.html')

@app.route('/countTwo', methods=['POST'])
def counter():
    if request.form['submit'] == 'addTwo':
        session['count'] += 1
    elif request.form['submit'] == 'reset':
        session['count'] = 0
    return redirect('/')

app.run(debug=True)