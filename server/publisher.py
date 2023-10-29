import random
import time
import ssl

from paho.mqtt import client as mqtt_client

broker = "ja5d193e.ala.us-east-1.emqxsl.com"
port = 8883
topic = "python/mqtt"

# Generate a Client ID with the publish prefix.
client_id = f"publish-{random.randint(0, 1000)}"

username = "sensor-app"
password = "sensor123"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("rc: ")
        print(rc)
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


def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        if msg_count > 5:
            break


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


if __name__ == "__main__":
    run()
