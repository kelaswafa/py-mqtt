import paho.mqtt.client as paho
import sys

from config import SERVER, PORT, TOPIC, QOS

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed : "+str(mid)+"\nGranted QoS : "+str(granted_qos[0])+"\n---------")

def on_message(client, userdata, msg):
    print("Topic : "+msg.topic+"\nQOS : "+str(msg.qos)+"\nMessage : "+str((msg.payload).decode('utf-8'))+"\n---------")    

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(SERVER, PORT)
client.subscribe(TOPIC, qos=QOS)

client.loop_forever()