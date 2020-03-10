from google_api import GooglePlaces
import googlemaps

APY_KEY = "AIzaSyD8eH8oVJgE4FeDTkSaU50z4XZL-q9mXaI"
google_api = googlemaps.Client(key = APY_KEY )
api = GooglePlaces(APY_KEY)

def getPlaces(adress):

	

	adress_json = google_api.geocode(adress)

	lat=adress_json[0]["geometry"]['location']['lat']
	lon=adress_json[0]["geometry"]['location']['lng']

	lat = str(lat)
	lon = str(lon)

	lat_lon = lat+","+lon

	places = api.search_places_by_coordinate(lat_lon, "500", "restaurant")

	return places
def getDetails(place,fields):
	details = api.get_place_details(place['place_id'], fields)
	return details