import random
import ssl
from paho.mqtt import client as mqtt_client

broker = "ja5d193e.ala.us-east-1.emqxsl.com"

port = 8883
topic = "python/mqtt"

# Generate a Client ID with the subscribe prefix.
client_id = f"subscribe-{random.randint(0, 100)}"

username = "sensor-app"
password = "sensor123"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)

    client.tls_set(
        ca_certs="ca_certificate/emqxsl-ca.crt",
        certfile=None,
        keyfile=None,
        cert_reqs=ssl.CERT_NONE,
        tls_version=ssl.PROTOCOL_TLS,
    )

    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == "__main__":
    run()
