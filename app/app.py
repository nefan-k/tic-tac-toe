from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/turn", methods = ['POST'])
def turn():
    data = {
        "status": "ongoing",
        "board": {
            0: "_",
            1: "_",
            2: "_",
            3: "_",
            4: "_",
            5: "_",
            6: "_",
            7: "X",
            8: "_"
        }
    }
    return jsonify(data)