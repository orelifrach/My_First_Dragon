from flask import Flask, request, render_template, redirect, session
from flask_session import Session
from pet import Pet

app = Flask("My First Dragon")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods =["GET", "POST"])
def test():
    if request.method == "POST":
        # name = request.form.get("name")
        return render_template("login.html")
    else:
        return render_template("home.html")
    

@app.get("/start")
def start():
    if request.form.get("name") == request.args.get("name"):
        type = request.args.get("type")
        name = request.args.get("name")
        # global pet
        pet = Pet(name, type)
        return render_template("home.html")
    return render_template("login.html")


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
