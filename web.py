from flask import Flask
from app import app
from pet import Pet

app = Flask("My First Dragon")

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/start/<type>/<name>')
def start(type, name):
    return f"{type}, {name}"

if __name__ == '__main__':
    app.run(port=5000)