from flask import Flask, request, render_template
from app import App
from pet import Pet

app = Flask("My First Dragon")
app.secret_key = "secret_key"
pet = None

@app.route('/')
def hello_world():
    return render_template("login.html")

@app.get('/start')
def start():
    global pet
    type = request.args.get('type')
    name = request.args.get('name')
    pet = Pet(name, type)
    return render_template("login.html")

@app.get('/status')
def get_status():
    global pet
    return pet.get_status()

@app.get('/show')
def get_data():
    global pet
    data = request.args.get('data')
    if data == "hunger":
        return pet.get_hunger()
    if data == "happiness":
        return pet.get_happiness()
    if data == "energy":
        return pet.get_energy()
    if data == "points":
        return pet.get_points()
    if data == "state":
        return pet.get_total_state()

@app.get('/eat')
def eat():
    global pet
    return pet.eat()

@app.get('/sleep')
def sleep():
    global pet
    return pet.sleep()

@app.get('/play')
def play():
    global pet
    return pet.play()

if __name__ == '__main__':
    app.run(port=5000)