import paho.mqtt.client as mqtt
import RPi.GPIO as gpio
from time import sleep

import defs

# MQTT setup
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("vend")

def on_message(client, userdata, msg):
    if msg.topic == "vend":
        print(f"Vending option {int(msg.payload)}")
        gpio.output(defs.PIN_SWITCH_OUT[int(msg.payload)], defs.OUT_HI)
        # This may or may not be a smart decision to sleep on this process.
        # Do I have a choice, though?
        sleep(0.5)
        gpio.output(defs.PIN_SWITCH_OUT[int(msg.payload)], defs.OUT_LO)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 9999)

# GPIO setup
gpio.setmode(gpio.BOARD)    # BOARD pin numbering

# Pullups can just be connected to 5VDC thru breadboard,
# no need to waste GPIOs there

# Pin setup, dfl low
for pin in defs.PIN_SWITCH_OUT:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, defs.OUT_LO)

# Just wait for MQTT
client.loop_forever()
