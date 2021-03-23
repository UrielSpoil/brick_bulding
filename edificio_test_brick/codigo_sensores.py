import os
import time
import sys
#import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
import json
import random as random

THINGSBOARD_HOST = 'iot.ier.unam.mx'
ACCESS_TOKEN = 'xPbwMvyG0IvGatCZOleI'   

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

sensor_data = {'temperature': 0, 'humidity': 0, 'iluminance': 0,'sound': 0 }

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)


# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
        humidity = random.uniform(0, 100)
        temperature = random.uniform(10, 60)
        iluminance = random.uniform(10, 60)
        sound = random.uniform(10, 60)

        humidity = round(humidity, 2)
        temperature = round(temperature, 2)
        iluminance = round(iluminance, 4)
        sound = round(sound, 4)
        print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%, Iluminance: {:g}lux, Sound: {:g}dB".format(temperature, humidity, iluminance, sound))
        sensor_data['temperature'] = temperature
        sensor_data['humidity'] = humidity
        sensor_data['iluminance'] = iluminance
        sensor_data['sound'] = sound

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()