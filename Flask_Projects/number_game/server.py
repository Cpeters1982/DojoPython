import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "KeepItSecret"

@app.route('/')
def index():
    try:
        session['answer']
    except KeyError:
        session['answer'] = random.randrange(0, 101)
    try:
        session['result']
    except KeyError:
        session['result'] = None
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess == session['answer']:
        session['result'] = 'correct'
    elif guess > session['answer']:
        session['result'] = 'high'
    elif guess < session['answer']:
        session['result'] = 'low'
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('answer')
    session.pop('result')
    return redirect('/')

app.run(debug=True)