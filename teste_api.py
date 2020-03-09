from google_api import GooglePlaces
import googlemaps

APY_KEY = "AIzaSyD8eH8oVJgE4FeDTkSaU50z4XZL-q9mXaI"
google_api = googlemaps.Client(key = APY_KEY )
api = GooglePlaces(APY_KEY)

adress = input("Insira o endereço: ")
adress_json = google_api.geocode(adress)

lat=adress_json[0]["geometry"]['location']['lat']
lon=adress_json[0]["geometry"]['location']['lng']

lat = str(lat)
lon = str(lon)

lat_lon = lat+","+lon

places = api.search_places_by_coordinate(lat_lon, "100", "restaurant")
fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
place = places[0]
details = api.get_place_details(place['place_id'], fields)
try:
    website = details['result']['website']
except KeyError:
    website = ""

try:
    name = details['result']['name']
except KeyError:
    name = ""

try:
    address = details['result']['formatted_address']
except KeyError:
    address = ""

try:
    phone_number = details['result']['international_phone_number']
except KeyError:
    phone_number = ""

try:
    reviews = details['result']['reviews']
except KeyError:
    reviews = []
print("===================PLACE===================")
print("Name:", name)
print("Website:", website)
print("Address:", address)
print("Phone Number", phone_number)
print("==================REWIEVS==================")
for review in reviews:
    author_name = review['author_name']
    rating = review['rating']
    text = review['text']
    time = review['relative_time_description']
    profile_photo = review['profile_photo_url']
    print("Author Name:", author_name)
    print("Rating:", rating)
    print("Text:", text)
    print("Time:", time)
    print("Profile photo:", profile_photo)
    print("-----------------------------------------")
