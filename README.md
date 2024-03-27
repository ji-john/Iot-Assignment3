# IoT Environmental Monitoring System

This project is an implementation of a cloud-based IoT system that collects data from virtual environmental stations using the MQTT protocol. The system simulates multiple environmental stations that periodically generate random sensor data (temperature, humidity, and CO2 levels) and publish it to a ThingSpeak channel.

## Requirements

- Python 3.x
- Paho MQTT library (`pip install paho-mqtt`)

## Setup

1. Clone the repository or download the source code.
2. Obtain your ThingSpeak channel ID and write API key. You can create a new channel on the ThingSpeak platform if you don't have one already.
3. Update the following variables in the code with your ThingSpeak credentials:
  - `channel_id`: Your ThingSpeak channel ID
  - `write_api_key`: Your ThingSpeak channel write API key

## Usage

1. Run the `IoT Sensor.py` script.
2. The script will simulate multiple environmental stations (default is 3) that publish sensor data to the specified ThingSpeak channel every 10 seconds for a duration of 60 seconds (default). You can modify these values by changing the arguments passed to the `simulate_stations` function call.
3. The published sensor data (temperature, humidity, and CO2 levels) will be displayed in the console output.

## File Structure

- `IoT Sesnsor.py`: Contains the main script that simulates the environmental stations and publishes data to ThingSpeak.
- `README.md`: This file, containing instructions and information about the project.

## Assignment Requirements

This project fulfills the following requirements of the assignment:

1. **Build a cloud-based IoT system that collects data from virtual sensors using the MQTT protocol**: The project simulates virtual environmental stations that generate random sensor data and publish it to a ThingSpeak channel using the MQTT protocol.

2. **Display the latest sensor data values received from all sensors of a specified environmental station**: To display the latest sensor data values, you can monitor the console output, which prints the data for each environmental station as it is published.

3. **Display the sensor data values received during the last five hours from all environmental stations for a specified sensor**: To display the sensor data values received during the last five hours, you can access the ThingSpeak channel data through the ThingSpeak API or by visualizing the data on the ThingSpeak platform.

Note: The project assumes that you have a ThingSpeak account and a channel set up. If you want to use a different cloud-based IoT backend, you may need to modify the code accordingly.
