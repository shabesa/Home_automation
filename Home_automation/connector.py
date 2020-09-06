import paho.mqtt.publish as pub
import paho.mqtt.subscribe as sub
from time import sleep

def send(msg):
     pub.single("command", payload=msg, qos=0, retain=False,
                hostname="localhost", port=1883, client_id="outTopic",
                keepalive=60, will=None, auth=None, tls=None,
                transport="tcp")
     print(msg + " sent")
     sleep(5)
     
     
     
def recieve(topic):
    data = sub.simple(topic, qos=0, msg_count=1, retained=False, hostname="localhost",
                       port=1883, client_id="inTopic", keepalive=60, will=None, auth=None, tls=None)
    print("%s %s" % (data.topic, data.payload))
    sleep(5)