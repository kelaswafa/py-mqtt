import paho.mqtt.client as paho
import time, random, sys

from config import SERVER, PORT, TOPIC, QOS

def on_publish(client, userdata, mid):
    print("Message %i success" % i)

client = paho.Client()
client.on_publish = on_publish
client.connect(SERVER, port=PORT)
client.loop_start()

i = 1
while True:
    (rc, mid) = client.publish(TOPIC, payload = i, qos=QOS)
    time.sleep(5)
    i += 1