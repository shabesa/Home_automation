from flask import Flask, render_template, request
import serial
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/control",methods=["POST"])
def control():
    if request.method == "POST":
        command = request.form.get('light')
        print(command)
        board.write(command.encode())
    return "success"   

if __name__=='__main__':
    board = serial.Serial("/dev/ttyUSB0", 9600)
    print(board)
    sleep(2)
    app.run()