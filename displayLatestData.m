% Set up ThingSpeak parameters
readChannelID = 2488354;
readAPIKey = 'X67UGUPLQ4AAMW95';

% Read latest sensor data from ThingSpeak channel
data = thingSpeakRead(readChannelID, 'ReadKey', readAPIKey, 'NumPoints', 1);

Temperature = data(1);
Humidity = data(2);
CO2 = data(3);

disp('Latest sensor data:');
disp('---------------------');
fprintf('Timestamp: %s\n', datestr(now));
fprintf('Temperature: %.2f °C\n', Temperature);
fprintf('Humidity: %.2f%%\n', Humidity);
fprintf('CO2: %.2f ppm\n', CO2);
