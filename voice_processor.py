import paho.mqtt.client as mqtt
import speech_recognition as sr
from random import randint

from subprocess import Popen as run     # Heresy, I know.

def say(message):
    run(["espeak", message])    # don't really care about stdout/err, just run in the background

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

# voice recognition setup

r = sr.Recognizer()

# Whether or not Sphinx is going to be able to recognize these words
# is anyone's guess.
drink_keywords = [
    ["polar", "orange vanilla", "number one", "option one"],
    ["lacroix", "tangerine", "number two", "option two"],
    ["vanilla coke", "vanilla", "coke", "number three", "option three"],
    ["orange soda", "fanta orange", "orange fanta", "orange", "fanta", "number four", "option four"],
    ["mystery flavor", "mystery", "number five", "option five"]
]

drink_names = [
    "polar seltzer",
    "tangerine seltzer",
    "vanilla coke",
    "orange fanta",
    "mystery beverage"
]

with sr.Microphone() as source:
    while True:
        print("Listening...")
        audio = r.listen(source)
        print("Processing...")

        try:
            text = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
            continue
        except sr.RequestError as e:
            print(f"Sphinx error: {e}")
            continue

        # Attempt to process whatever the fuck this person just said
        if "please" in text:
            if "surprise me" not in text:
                for idx, keyword_set in drink_keywords:
                    if any(keyword in text for keyword in keyword_set):
                        say(f"Enjoy your refreshing {drink_names[idx]}")
                        client.publish(vend, idx)
                        break
                else:
                    print(f"Recognized text \"{text}\" does not match any keywords.")
                    say("I don't understand.")
            else:
                say("Consider yourself surprised.")
                client.publish("vend", random.choice(range(len(defs.PIN_SWITCH_OUT)))
        else:
            say(f"You need to say the magic word.")
