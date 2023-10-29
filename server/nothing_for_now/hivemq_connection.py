import time

import paho.mqtt.client as paho
from paho import mqtt


def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))


def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.tls_insecure_set(True)

client.username_pw_set("sensor-app", "sensor123")


# cluster url
client.connect("b0496b3f1cf64a2489cafdfdb1903130.s2.eu.hivemq.cloud", 1883)

client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# topic name
client.subscribe("device/lidar/data", qos=0)

# arg 1 = topic name, arg 2 = message to send
# client.publish("device/lidar/data", payload="hello", qos=0)

client.loop_forever()
