#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:52:56 2018

@author: nathancaplan
"""
#Import Libraries
from __future__ import print_function
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
    
#Tell the script what arguements (i.e API key and bus number) should be read from the terminal
key = str(sys.argv[1])
bus_line = str(sys.argv[2])
csv_filename = str(sys.argv[3])

#Print the busline
print("Bus Line : " + bus_line)

#Create the json file's url
url1 = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2 = "&VehicleMonitoringDetailLevel=calls&LineRef="
full_url = url1 + key + url2 + bus_line

#Read the json file and collect the data from Vehicle activity
response = urllib.urlopen(full_url)
data = response.read().decode('utf-8')
data = json.loads(data)
Bus_data = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Latitude, Longitude, Stop Name, Stop Status")

#Create a data frame and populate it with the data from OnwardCalls dictionary
#The dataframe is the concatenation of each row
write_data = pd.DataFrame()
for i in Bus_data: 
    print(str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + "," +  str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']) + "," + str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']) + ',' + str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']))
    empty_list = []
    empty_list.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    empty_list.append(str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    if (len(i['MonitoredVehicleJourney']['OnwardCalls'])== 0):
        empty_list.append('N/A')
        empty_list.append('N/A')
    else: 
        empty_list.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']))
        empty_list.append(str(i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']))
    new_data = pd.DataFrame(data=[empty_list])
    write_data = pd.concat([write_data,new_data], axis =0)

#Organize the dataframe with column titles and the index reset
write_data.columns = ['Latitude','Longitude','Stop Name','Stop Status']
write_data.reset_index()
    
#Write the dataframe to a csv
write_data.to_csv(csv_filename)
        

        

    



    
    