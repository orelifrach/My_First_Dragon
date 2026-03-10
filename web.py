from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from pet import Pet
from database import database

app = Flask("My First Dragon")
db = database()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["POST", "GET"])
def test():
    if request.method == "GET":
        return render_template("start.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        pet = db.get_pet(username, password)
        return request.get("/start", params={"pet": pet}).text()
    
    

@app.get("/start")
def start():
    if len(request.args.getlist()) > 1:
        pet_type = request.args["pet_type"]
        pet_name = request.args["pet_name"]
        # global pet
        pet = Pet(pet_name, pet_type)
    else:
        pet = request.args["pet"]
    return render_template("home.html")


@app.get("/status")
def get_status():
    return pet.get_status()


@app.get("/show")
def get_data():
    data = request.args.get("data")
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


@app.get("/eat")
def eat():
    return pet.eat()


@app.get("/sleep")
def sleep():
    return pet.sleep()


@app.get("/play")
def play():
    return pet.play()


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
