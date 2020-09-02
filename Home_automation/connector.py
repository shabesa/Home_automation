import paho.mqtt.client as mqtt
import time

def bridge():
    def on_log(client, userdata, level, buf):
        print("log: " +buf)


    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("connected")
        else:
            print("Bad connection Return code",rc)


    def on_disconnect(client, userdata, flags, rc=0):
        print("Disconnected result code"+str(rc))

    def on_message(client, userdata, msg):
        topic=msg.topic
        m_decode=str(msg.payload.decode("utf-8","ignore"))
        print("message recieved", m_decode)

    broker="192.168.0.106"
    client = mqtt.Client("Home_auto_main")

    client.on_connect=on_connect
    client.on_disconnect=on_disconnect
    client.on_log=on_log
    client.on_message=on_message

    print("connecting to broker",broker)
    client.connect(broker)
    client.subscribe("outTopic")
    client.loop_forever()