import phonenumbers
from app import number
import folium

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))

location = geocoder.description_for_number(ch_number,"en")

import opencage
from opencage.geocoder import OpenCageGeocode
key = '831700a26df246a49d2fd85e9859e1ae'
geocoder =OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat =results[0]['geometry']['lat']
lng =results[0]['geometry']['lng']
print(lat,lng)

mymap = folium.Map(location=[lat,lng], zoom_start= 9)
folium.Marker([lat,lng], popup=location).add_to(mymap)
mymap.save("mylocation.html")


# ---------------
# stackify website
# IPSTack key
# https://stackify.com/python-geocoder-a-guide-to-managing-locations-in-your-apps/
#----------------
import requests
key = "e88e972426c5be7ed2b8a1a45b4460dd"
ip = "2.216.185.49"
url = "http://api.ipstack.com/" + ip +"?access_key=" + key
response = requests.get(url).json()
print(response)

def lng_lat_from_ip(ip):
	url = "http://api.ipstack.com/" + ip + "?access_key=" + key 
	response = requests.get(url).json()
	return (response['longitude'], response['latitude']) 
longitude, latitude = lng_lat_from_ip(ip)

# def lng_lat_from_ip(ip):
# 	url = "http://api.ipstack.com/" + ip + "?access_key=" + key 
# 	response = requests.get(url).json()
# 	return (response['longitude'], response['latitude']) 
# longitude, latitude = lng_lat_from_ip(ip)
# print("second function+ ' 	'+ longitude,latitude")

from geopy.distance import geodesic
Brighton = (longitude, latitude) # I used our function above to get this.
cleveland_oh = (41.499498, -81.695391) # I looked this one up.
print("distance		" ,geodesic(Brighton, cleveland_oh).miles)


# for tracing weather information from IP
# import requests
# username = "mughali4"
# def weather_from_lat_lng(lat, lng):
# 	url="http://api.geonames.org/findNearByWeatherJSON?lat=" + lat + "&lng=" + lng + "&username=" + username
# 	response = requests.get(url).json()
# 	return response
# print(weather_from_lat_lng("41.499498", "-61.695391"))

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')