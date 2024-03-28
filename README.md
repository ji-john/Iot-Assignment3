# IoT Environmental Monitoring System

This project is an implementation of a cloud-based IoT system that collects data from virtual environmental stations using the MQTT protocol. The system simulates multiple environmental stations that periodically generate random sensor data (temperature, humidity, and CO2 levels) and publish it to a ThingSpeak channel.

## Requirements

- Python 3.x
- Paho MQTT library (`pip install paho-mqtt`)
- Thinkspeak

## Setup

1. Clone the repository or download the source code.
2. Obtain your ThingSpeak channel ID and write API key. You can create a new channel on the ThingSpeak platform if you don't have one already. Also create the MQTT device setup
3. Update the following variables in the code with your ThingSpeak credentials:
  - `channel_id`: Your ThingSpeak channel ID
  - `write_api_key`: Your ThingSpeak channel write API key
`MQTT Credentials`:
  - `MQTT Client ID`
  - 'Username`
  - `Password'

## Usage

1. Run the `IoT Sensor.py` script.
2. The script will simulate multiple environmental stations (default is 3) that publish sensor data to the specified ThingSpeak channel every 10 seconds for a duration of 60 seconds (default). You can modify these values by changing the arguments passed to the `simulate_stations` function call.
3. The published sensor data (temperature, humidity, and CO2 levels) will be displayed in the console output.

## File Structure

- `IoT Sesnsor.py`: Contains the main script that simulates the environmental stations and publishes data to ThingSpeak.
- `displayLatestData.m`: A MATLAB script for displaying the latest sensor data values from all sensors of a specified environmental station. Connects to ThingSpeak to fetch the most recent data.
- `displayHistoricalData.m`: Another MATLAB script designed to display sensor data from the last five hours from all environmental stations for a specific sensor, providing trend analysis and monitoring.
- `README.md`: This file, containing instructions and information about the project.


## Latest Sensor Data Display

A MATLAB script (displayLatestData.m) has been developed to display the latest sensor data values from all sensors of a specified environmental station. This script connects to the ThingSpeak channel and fetches the most recent data entries for each sensor type. It provides real-time data visualization, showcasing the latest readings from temperature, humidity, and CO2 sensors.

## Last Five Hours Data Display

Another MATLAB script (displayHistoricalData.m) is included for visualizing sensor data received during the last five hours from all environmental stations for a specific sensor. This script retrieves historical data from the ThingSpeak channel, allowing for an analysis of trends and patterns over a five-hour period. The script can be customized to focus on a particular sensor type and provides a detailed view of the environmental changes monitored by the system.

Note: The project assumes that you have a ThingSpeak account and a channel set up. If you want to use a different cloud-based IoT backend, you may need to modify the code accordingly.
