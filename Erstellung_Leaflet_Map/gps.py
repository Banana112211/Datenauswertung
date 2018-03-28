# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:02:03 2017

@author: Gustav Willig
"""

import folium
import numpy as np
import pandas as pd
import numpy.ma as ma
import base64
import matplotlib.pyplot as plt
from folium import IFrame
 
def Erstellung_Map_aus_GPS(file_name):
    """Erstellung aus einer .csv eine leaflet-Map. Wichtig ist dabei, dass dabei in der dritten Spalte Latitude ist und in der 5 Spalte Longitude """
    #1.Step: read gps_data from txt
    txt_gps = open(file_name)

    gps_data=[]
    for i in txt_gps:
       line=i.split(",")
       gps_data.append(line)
    
    resolution, width, height = 75, 7, 3
    lon, lat = 9.21006966667, 49.1234218333
    map1 = folium.Map(location=[lat, lon], zoom_start=17)
     
    encoded = base64.b64encode(open('marker.png', 'rb').read()).decode()
     
    html = '<img src="data:image/png;base64,{}">'.format
    iframe = IFrame(html(encoded), width=632+20, height=420+20)
    popup = folium.Popup(iframe, max_width=2650)
    
    
    fg=folium.FeatureGroup(name="MyMap")
    
    icon1 = folium.Icon(color="red", icon="ok")
    
    icon2 = folium.Icon(color="red", icon="ok")
    
    for row in range(1,len(gps_data)): # In row 0 stehe die Ueberschriften, daher beginnt es in Row 1
           test1=float(gps_data[row][2].strip("'"))
           test2=float(gps_data[row][4].strip("'"))
           fg.add_child(folium.Marker(location=[test1,test2], popup=str(gps_data[row][1]), icon=folium.Icon(color='green')));
    map1.add_child(fg)
    map1.save("Map.html")

if __name__ == "__main__":
    Erstellung_Map_aus_GPS("gps Wed Mar 28 10_56_06 2018.csv")
