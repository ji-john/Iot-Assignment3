% Set up ThingSpeak parameters
readChannelID = 2488354;
readAPIKey = 'X67UGUPLQ4AAMW95';

% Calculate the start and end times for the last 5 hours
endTime = datetime('now'); % Current datetime
startTime = endTime - hours(5); % 5 hours ago

% Read sensor data from ThingSpeak channel for the last 5 hours
data = thingSpeakRead(readChannelID, 'ReadKey', readAPIKey, 'DateRange', [startTime endTime]);

% Extract the temperature, humidity, and CO2 data
Temperature = data(:, 1);
Humidity = data(:, 2);
CO2 = data(:, 3);
Timestamps = startTime + minutes((1:numel(Temperature))-1); % Generate timestamps based on the start time and interval

disp('Sensor data for the last 5 hours from all environmental stations:');
disp('-----------------------------------------------------------------');

% Display the data for each timestamp
for i = 1:length(Timestamps)
    fprintf('Timestamp: %s\n', datestr(Timestamps(i)));
    fprintf('Temperature: %.2f °C\n', Temperature(i));
    fprintf('Humidity: %.2f%%\n', Humidity(i));
    fprintf('CO2: %.2f ppm\n\n', CO2(i));
end
