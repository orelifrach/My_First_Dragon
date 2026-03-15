from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from pet import Pet
from database import database
import ctypes

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
        # return redirect("/start?pet_name=puppy&pet_type=dog")
        # need to understand how to send the instance
        return redirect(f"/start?pet={pet}")

@app.get("/start")
def start():
    counter = 0
    for i in request.args.values():
        counter += 1
    print(counter)
    pet = None
    if counter > 1:
        pet_type = request.args["pet_type"]
        pet_name = request.args["pet_name"]
        # global pet
        pet = Pet(pet_name, pet_type)
    else:
        pet_repr = request.args.get("pet")
        pet = repr_to_pet(pet_repr)
    # return render_template("home.html")
    return redirect(f"/home?pet={pet}")

@app.get("/home")
def home():
    pet_repr = request.args.get("pet")
    return render_template("home.html", pet_repr=pet_repr)

@app.get("/status")
def get_status():
    return pet.get_status()

@app.get("/show")
def get_data():
    data = request.args.get("data")
    pet_repr = request.args.get("pet_repr")
    pet = repr_to_pet(pet_repr)
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

def repr_to_pet(pet_repr):
    pet_hex = (pet_repr.split(" ")[-1][:-1])
    pet_id = int(pet_hex, 16)
    pet = ctypes.cast(pet_id, ctypes.py_object).value
    return pet

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
