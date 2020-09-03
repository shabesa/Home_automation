from flask import Flask, render_template, request
import paho.mqtt.publish as pub
import paho.mqtt.subscribe as sub
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
            pub.single("command", payload="on", qos=0, retain=False,
                       hostname="localhost", port=1883, client_id="outTopic",
                       keepalive=60, will=None, auth=None, tls=None,
                       transport="tcp")
            msg = sub.simple("feedback", qos=0, msg_count=1, retained=False, hostname="localhost",
                       port=1883, client_id="inTopic", keepalive=60, will=None, auth=None, tls=None)
            print("%s %s" % (msg.topic, msg.payload))
        
        elif command == "off":
            pub.single("command", payload="off", qos=0, retain=False,
                       hostname="localhost", port=1883, client_id="outTopic",
                       keepalive=60, will=None, auth=None, tls=None,
                       transport="tcp")
   
   return "success"   




if __name__=='__main__':
    board = serial.Serial("/dev/ttyUSB0", 9600)
    print(board)
    sleep(2)
    app.run()