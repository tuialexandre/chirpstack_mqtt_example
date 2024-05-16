import paho.mqtt.client as mqtt

topic = "#"
host_address = "192.168.0.181"
host_port = 1883
mqtt_username = "radioenge"
mqtt_password = "radioenge"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="")
mqttc.username_pw_set(username=mqtt_username, password=mqtt_password)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect(host=host_address, port=host_port, keepalive=60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()
