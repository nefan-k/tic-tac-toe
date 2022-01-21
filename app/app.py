from flask import Flask, render_template, jsonify, request
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/turn", methods = ['POST'])
def turn():
    incoming = request.get_json()
    print(incoming)
    
    updated_board = player_turn(incoming["id"], incoming["board"])
    # check if game is ended -> return status and board as is
    status = check(updated_board)

    # if NOT:
    #   make our turn & check
    if status == "ongoing":
        updated_board = cpu_turn(updated_board)
        status = check(updated_board)

    # return board with OUR and Player's turns
    outgoing = {
        "status": status,
        "board": updated_board
    }
    return jsonify(outgoing)

def check(board):
    for i in range(0, 7, 3):
        if board[str(i)] == board[str(i+1)] == board[str(i+2)]:
            if board[str(i)] == "_":
                continue
            elif board[str(i)] == "X":
                return "winner"
            elif board[str(i)] == "O":
                return "looser"
    
    for i in range(3):
        if board[str(i)] == board[str(i+3)] == board[str(i+6)]:
            if board[str(i)] == "_":
                continue
            elif board[str(i)] == "X":
                return "winner"
            elif board[str(i)] == "O":
                return "looser"

    if board["0"] == board["4"] == board["8"]:
        if board["4"] == "X":
            return "winner"
        elif board["4"] == "O":
            return "looser"
    
    if board["2"] == board["4"] == board["6"]:
        if board["4"] == "X":
            return "winner"
        elif board["4"] == "O":
            return "looser"

    if len(get_empty(board)) == 0:
        return "draft"

    return "ongoing"
      

def cpu_turn(board):
    e_spaces = get_empty(board)
    i = randint(0, len(e_spaces) - 1)
    board[e_spaces[i]] = "O"
    return board

def get_empty(board):
    e_spaces = []
    for key in board:
        if board[key] == "_":
            e_spaces.append(key)
    return e_spaces

def player_turn(id, board):
    if board[id] == "_":
        board[id] = "X"

    return board
