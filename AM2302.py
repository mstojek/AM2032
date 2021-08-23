
import os
import sys
from requests.auth import HTTPBasicAuth
import requests
import adafruit_dht
from board import D4

domoticz_ip='127.0.0.1'
domoticz_port='8080'
user=''
password=''
domoticz_idx=1

dht_device = adafruit_dht.DHT22(D4)
temperature = dht_device.temperature
humidity = dht_device.humidity

if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
else:
        print("Failed to retrieve data from humidity sensor")

def maj_widget(val_url):
    requete='http://'+domoticz_ip+':'+domoticz_port+val_url
    #print requete
    r=requests.get(requete,auth=HTTPBasicAuth(user,password))
    if  r.status_code != 200:
          print( "Erreur API Domoticz")

if humidity is not None and temperature is not None:

    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    # l URL Domoticz pour le widget virtuel
    url='/json.htm?type=command&param=udevice&idx='+str(domoticz_idx)
    url+='&nvalue=0&svalue='
    url+=str('{0:0.1f};{1:0.1f};2').format(temperature, humidity)
    #print url
    maj_widget(url)

else:
    print('Probleme avec la lecture du DHT. Try again!')
    sys.exit(1)
