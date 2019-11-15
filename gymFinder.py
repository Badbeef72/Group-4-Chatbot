# Importing libraries 
from googleplaces import GooglePlaces, types, lang 
import requests 
import json 
  


API_KEY = 'AIzaSyD2U1i-Dh-8nhPkf65GLNwDBGk2mgtf6ls'
  

google_places = GooglePlaces(API_KEY) 

def findLocation(lat,lng,rad):
    query_result = google_places.nearby_search( 
        lat_lng ={'lat': lat, 'lng': lng}, 
        radius = rad,          
        types =[types.TYPE_GYM])
    if query_result.has_attributions: 
        print (query_result.html_attributions)
    for place in query_result.places:
        print (place.name) 
        print("Latitude", place.geo_location['lat']) 
        print("Longitude", place.geo_location['lng']) 
        print()
          
def mile_to_rad(mile):
    rad = mile * 1000
    return rad
    
    

  
print("Please find your longitude and latitude online before using this")
lat = input("Enter Your Latitude: ")
lng = input("Enter Your Longitude: ")
user_mile = int(input("Enter how far away you want to look in miles: "))
findLocation(lat,lng,mile_to_rad(user_mile))

        
        
