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

@app.get("/")
def open():
    return render_template("open.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        pet_type = request.form["pet_type"]
        pet_name = request.form["pet_name"]
        pet = Pet(pet_name, pet_type)
        db.insert_pet(username, password, pet)
        return redirect(f"/home?pet_repr={pet}")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        pet = db.get_pet(username, password)
        return redirect(f"/home?pet_repr={pet}")

# @app.get("/getin")
# def get_in():
#     print("LOL")
#     counter = 0
#     for _ in request.args.values():
#         counter += 1
#     print(counter)
#     pet = None
#     if counter > 1:
#         pet_type = request.args["pet_type"]
#         pet_name = request.args["pet_name"]
#         pet = Pet(pet_name, pet_type)
#         return redirect(f"/home?pet_repr={pet}")
#     else:
#         pet_repr = request.args.get("pet_repr")
#         return redirect(f"/home?pet_repr={pet_repr}")
#     # return render_template("home.html")

@app.get("/home")
def home():
    pet_repr = request.args.get("pet_repr")
    return render_template("home.html")

@app.get("/status")
def get_status():
    return pet.get_status()

@app.get("/show")
def get_data():
    data = request.args.get("pet")
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
    pet_id = id(pet_repr)
    pet = ctypes.cast(pet_id, ctypes.py_object).value
    return pet

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
