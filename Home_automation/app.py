from flask import Flask, render_template, request
from connector import send, recieve
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
        '''writing to control board'''
        board.write(command.encode())
        '''publish and subscribe via mqtt'''
        if command == "on":
            send("on")
            recieve("feedback")
        
        elif command == "off":
            send("off")
            recieve("feedback")
   
    return "success"   




if __name__=='__main__':
    board = serial.Serial("/dev/ttyUSB0", 9600)
    print(board)
    sleep(2)
    app.run()