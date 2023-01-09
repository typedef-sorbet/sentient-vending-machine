import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
from time import sleep

import defs

# MQTT setup
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

def on_message(client, userdata, msg):
    # This will be a publisher process, so there's really no need for this function
    print(f"{msg.topic}: {msg.payload}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 9999)

# GPIO setup
def pin_callback(pin):
    print(f"Pin {pin} has posedge")
    client.publish("vend", defs.PIN_SWITCH_IN.idx(pin))

gpio.setmode(gpio.BOARD)    # BOARD pin numbering

# Pullups can just be connected to 5/3.3VDC thru breadboard,
# no need to waste GPIOs there

for pin in defs.PIN_SWITCH_IN:
    gpio.setup(pin, gpio.IN)
    gpio.add_event_detect(pin, gpio.RISING, callback=pin_callback, bouncetime=200)

while True:
    # Event loop while we wait for events to come in from GPIO
    pass
