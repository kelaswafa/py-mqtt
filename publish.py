import paho.mqtt.client as paho
import time, random, sys

from config import SERVER, PORT, TOPIC, QOS
 
    
client = paho.Client()
client.on_publish = lambda _, __, mid : print("Message %i success" % mid)
client.connect(SERVER, port=PORT)
client.loop_start()

i = 1
while True:
    (rc, mid) = client.publish(TOPIC, payload = i, qos=QOS)
    time.sleep(5)
    i += 1