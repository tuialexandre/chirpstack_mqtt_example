import paho.mqtt.client as mqtt


application_id = "04f855fb-fd17-4cd1-b5c5-51d7b15e3730"
devEui = "0012f800000029a6"
fPort = 10
data = "QVQrU0VORD0zOnRlc3Rl"

host_address = "192.168.0.181"
host_port = 1883
mqtt_username = "radioenge"
mqtt_password = "radioenge"

# Chirpstack downlink topic format: application/[ApplicationID]/device/[DevEUI]/command/down
topic = f"application/{application_id}/device/{devEui}/command/down"
payload = (
    f'{{"devEui": "{devEui}", "confirmed": false, "fPort": {fPort}, "data": "{data}"}}'
)


def on_connect(mqttc, obj, flags, reason_code, properties):
    print("reason_code: " + str(reason_code))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid, reason_code, properties):
    print("mid: " + str(mid))


mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="")
mqttc.username_pw_set(username=mqtt_username, password=mqtt_password)


mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

mqttc.connect(host=host_address, port=host_port, keepalive=60)

mqttc.loop_start()

infot = mqttc.publish(topic, payload, qos=2)

infot.wait_for_publish()