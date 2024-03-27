pip install paho-mqtt

import random
import string
import time
import uuid
import paho.mqtt.client as mqtt

client_id = "MxsePSYuKRgfHisvGiMPMDQ"
channel_id = "2488354"
write_api_key = "ZS7CJ5AJ1HFVTOC4"

class EnvironmentalStation:
    def __init__(self, mqtt_client):
        self.id = uuid.uuid4()
        self.mqtt_client = mqtt_client
        self.temperature_range = (-50, 50)
        self.humidity_range = (0, 100)
        self.co2_range = (300, 2000)

    def generate_sensor_data(self):
        temperature = random.uniform(*self.temperature_range)
        humidity = random.uniform(*self.humidity_range)
        co2 = random.uniform(*self.co2_range)
        return {'temperature': temperature, 'humidity': humidity, 'co2': co2}

    def publish_data(self, mqtt_client, channel_id, write_api_key):
      sensor_data = self.generate_sensor_data()
      print(f"Station {self.id} Data: {sensor_data}")
      payload = "field1=" + str(sensor_data['temperature']) + "&field2=" + str(sensor_data['humidity']) + "&field3=" + str(sensor_data['co2'])
      topic = f"channels/{channel_id}/publish"
      mqtt_client.publish(topic, payload)

def simulate_stations(n_stations, duration, frequency, mqtt_client):
    stations = [EnvironmentalStation(mqtt_client) for _ in range(n_stations)]
    start_time = time.time()
    while time.time() - start_time < duration:
        for station in stations:
            station.publish_data(mqtt_client, channel_id, write_api_key)
        time.sleep(frequency)

# MQTT Client setup
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,client_id=client_id)
mqtt_client.username_pw_set(username="MxsePSYuKRgfHisvGiMPMDQ", password="l1GykJSEZHG7TX6TF+OSnIbN")

# Start the MQTT client loop
mqtt_client.loop_start()

# Connect to the MQTT broker
mqtt_client.connect("mqtt3.thingspeak.com", 1883)

# Example usage: Simulating 3 stations for 60 seconds with data generation every 10 seconds
simulate_stations(3, 60, 10, mqtt_client)

# Stop the MQTT client loop
mqtt_client.loop_stop()