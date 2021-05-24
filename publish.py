import time

import paho.mqtt.client as paho

from config import PORT, QOS, SERVER, TOPIC


def on_publish(client, userdata, mid):
    print("Message %i success" % i)

client = paho.Client()
client.on_publish = on_publish
client.connect(SERVER, port=PORT)
client.loop_start()

i = 1
while True:
    payload = "Pesan ke-%i" % i
    (rc, mid) = client.publish(TOPIC, payload=payload, qos=QOS)
    time.sleep(5)
    i += 1
