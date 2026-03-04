from flask import Flask, request
from app import app
from pet import Pet

app = Flask("My First Dragon")

@app.route('/')
def hello_world():
    return 'Hello World'

@app.get('/start/get')
def start():
    type = request.args.get('type')
    name = request.args.get('name')
    new = Pet(name, type)
    return new.get_status()

if __name__ == '__main__':
    app.run(port=5000, )