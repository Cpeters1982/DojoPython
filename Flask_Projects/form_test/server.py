'''
Form_test assignment from CodingDojo
'''
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'KeepItSecret'

@app.route('/')
def index():
  # print "index route"
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
  #  print "users route, got post data"
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/show')

@app.route('/show')
def show_user():
  # print "show_user route"
  return render_template('user.html')# , name = session['name'], email = session['email']

# @app.route('/process', methods=['POST'])
# def process():
#   if request.form['action'] == 'register':
#     # Do registration process
#   elif request.form['action'] == 'login':
#     # Do login process
# return ()
app.run(debug=True)
# We can basically copy the session data from server.py
# into our templates using the same line but encased in {{}}
# That is as valid as putting session['var'] in our show_user function
# but it looks much nicer in the template...also easier to test
# Remember that a simple print statement is a pretty good test to make sure
# we are hitting our routes.
