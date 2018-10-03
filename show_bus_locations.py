=# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 
import sys
import numpy as np
import pandas as pd
import pylab as pl
import json
try: 
    import urllib2 as urllib
except ImportError: 
    import urllib.request as urllib  
    
key = str(sys.argv[1])
bus_line = str(sys.argv[2])
    
print("Bus Line : " + bus_line)

url1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="

full_url = url1 + key + url2 + bus_line

response = urllib.urlopen(full_url)
data = response.read().decode('utf-8')
 data = json.loads(data)
Bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Number of Active Buses: " + str(len(Bus_data)))

Bus_Info = 0
for i in Bus_data: 
    print("Bus " + str(Bus_Info) + " is at lattitude " +  str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + " and longitude " +  str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    Bus_Info += 1