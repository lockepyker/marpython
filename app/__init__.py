# I'm a single line comment! 
from flask import Flask, url_for, render_template
#from flask import url_for

app = Flask(__name__)
@app.route('/')
def helloJoel():
    return "Hello Joel!"

@app.route('/test')
def test():
    return "I'm a test page"

# url_for('static', filename='favicon.ico') 
# url_for('static', filename='main.css')
# pip freeze > requirements.txt imports all dependencies to .txt
# create hello.py and run exactly as example in documentation
# namespace = all functions and variables associated with your program

#from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>') # <name> is a wildcard, but must be defined within
# def hello_route_handler(name=None):
#    name_string = 'hello world!'
#    if name:
#      name_string = 'hello {name}'.format(name)
#   return render_template('hello.html', name=name_string) something is not right here

# construct full template, header body, config static assest NOT HERE

def hello(name=None):
    return render_template('hello.html', name=name)