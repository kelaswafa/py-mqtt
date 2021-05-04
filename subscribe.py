import paho.mqtt.client as paho
import sys

from config import SERVER, PORT, TOPIC, QOS

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed\t:", mid)
    print("Granted QoS\t:", granted_qos[0])
    print("-"*10)

def on_message(client, userdata, msg):
    print("Topic\t:", msg.topic)
    print("QOS\t:", msg.qos)
    print("Message\t:", msg.payload.decode('utf-8'))
    print("-" *10)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(SERVER, PORT)
client.subscribe(TOPIC, qos=QOS)

client.loop_forever()