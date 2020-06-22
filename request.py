import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'AIRLINE':1,'FLIGHT_NUMBER':98,'SCHEDULED_DEPARTURE':5,'DEPARTURE_TIME':2345,'DEPARTURE_DELAY':-16,'SCHEDULED_ARRIVA':403,'ARRIVAL_TIME':409})

print(r.json())

