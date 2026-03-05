from flask import Flask, request, render_template
from pet import Pet

app = Flask("My First Dragon")
app.secret_key = "secret_key"


@app.get("/start")
def start():
    if "pet" not in globals():
        type = request.args.get("type")
        name = request.args.get("name")
        global pet
        pet = Pet(name, type)
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
    app.run(port=5000)
