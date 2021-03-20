import paho.mqtt.client as paho
import time
import random

def on_publish(client, userdata, mid):
    print("client : "+str(client))
    print("userdata : "+str(userdata))
    print("mid : "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect("www.mqtt-dashboard.com", port=1883)
client.loop_start()

while True:
    temperature = random.randint(0, 5000000)
    (rc, mid) = client.publish("8d1db723-c4b7-465e-8761-6d4e59ed4b74/4107847c-be59-4bf9-ab84-6424a80c28e0", payload = str(temperature), qos=0)
    time.sleep(5)