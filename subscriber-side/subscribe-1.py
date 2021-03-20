import paho.mqtt.client as paho

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed : "+str(mid)+"\nGranted QoS : "+str(granted_qos[0])+"\n---------")

def on_message(client, userdata, msg):
    print("Topic : "+msg.topic+"\nQOS : "+str(msg.qos)+"\nMessage : "+str((msg.payload).decode('utf-8'))+"\n---------")    

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("www.mqtt-dashboard.com", 1883)
client.subscribe("8d1db723-c4b7-465e-8761-6d4e59ed4b74/4107847c-be59-4bf9-ab84-6424a80c28e0", qos=0)

client.loop_forever()