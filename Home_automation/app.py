from flask import Flask, render_template, request
from flask_mqtt import Mqtt
import serial
from time import sleep

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'localhost'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAMER'] = ''
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True

mqtt = Mqtt(app)

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
            mqtt.publish('command', 'on')
        
        elif command == "off":
            mqtt.publish('command', 'off')
   
    return "success"
    sleep(2)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('feedback')



@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data)

if __name__=='__main__':
    board = serial.Serial("/dev/ttyUSB0", 9600)
    print(board)
    sleep(2)
    app.debug=True
    app.run()
