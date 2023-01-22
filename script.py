import pprint
# import requests
# from matplotlib import pyplot as plt
from datetime import datetime

# here we are formatting the PrettyPrinter. Try using different indents!
pp = pprint.PrettyPrinter(indent=4)
API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'seattle' 
# r = requests.get(API_URL + city)

# below is a mok response as the URL is broken 
response = {
    'description': 'Partly cloudy',
    'forecast': [ {'day': '1', 'temperature': '+22 °C', 'wind':'12 km/h'},
                  {'day': '2', 'temperature': '+15 °C', 'wind':'14 km/h'},
                  {'day': '3', 'temperature': '+5 °C', 'wind':'4 km/h'}],
    'temperature': '21 °C',
    'wind': '9 km/h'
}
pp.pprint(response)

forecast_list = response['forecast']
today = datetime.now().strftime("%b-%d-%Y")

to_graph = {} # The empty dictionary to store our shaped data
count = 1 # A global iterator to track each day past current datetime

for day in forecast_list:
    current_date = int(today[4:6]) + count
    this_day = f"{today[0:4]}{current_date}{today[6:]}"
    count += 1

    to_graph[this_day] = day['wind']
print(to_graph)

# Remember to always label the axes of your graph!
plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')

print('to_graph keys: ', to_graph.keys())
print('to_graph values: ', to_graph.values())

plt.scatter(to_graph.keys(), to_graph.values()) # sets up the graph
plt.show() # paints the graph to your screen

