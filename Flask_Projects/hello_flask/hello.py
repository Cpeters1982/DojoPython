# pylint: disable=invalid-name
'''
Initial flask project.
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
  '''
  Defines a function hello_world, which points to index.html. Standard GET route.
  '''
  return render_template('index.html')

@app.route('/success')

def success():  
  '''
  Another GET route, points to success.html
  '''
  return render_template('success.html')

app.run(debug=True)

# Our route rules define what comes after the initial forward-slash. When a request matching our routing rule is received by the server, 
# the function that immediately follows the @app.route('/some_route') is invoked.