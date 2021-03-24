import paho.mqtt.client as paho
import time, random, sys

sys.path.append('..')
from config import SERVER, PORT, TOPIC, QOS

def on_publish(client, userdata, mid):
    print("client : "+str(client))
    print("userdata : "+str(userdata))
    print("mid : "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect(SERVER, port=PORT)
client.loop_start()

while True:
    temperature = random.randint(0, 5000000)
    (rc, mid) = client.publish(TOPIC, payload = str(temperature), qos=QOS)
    time.sleep(5)