import time

import machine
from umqtt.simple import MQTTClient
from machine import Pin


piezo = machine.Pin(0, Pin.IN)

# Default MQTT server to connect to
SERVER = "192.168.0.XXX"
CLIENT_ID = "Doorbell Sensor"
TOPIC = b"doorbell"


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server)
    c.connect()
    threshold = 256
    print("Connected to %s, waiting for ring" % server)
    while True:
        while True:
            if piezo.value() > threshold:
                break
            time.sleep_ms(20)
        print("Ring")
        c.publish(TOPIC, b"ON")
        time.sleep_ms(200)

c.disconnect()