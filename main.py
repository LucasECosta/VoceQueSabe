from flask import Flask
import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from api import getPlaces,getDetails
from google_api import GooglePlaces
import googlemaps


APY_KEY = "AIzaSyD8eH8oVJgE4FeDTkSaU50z4XZL-q9mXaI"
google_api = googlemaps.Client(key = APY_KEY )
api = GooglePlaces(APY_KEY)
valid_types = [line.rstrip('\n') for line in open('valid_types.txt')]
name_types =[line.rstrip('\n').replace("_"," ").title() for line in open('valid_types.txt')]

app = Flask(__name__)



@app.route('/')
def main():


    return render_template('index.html',valid_types=valid_types,name_types=name_types)

@app.route('/', methods=['GET','POST'])
def results():
    adress = request.form['adress']
    type_places = request.form['time']
    #Executa a função de buscar endereços próximos.
    places = getPlaces(adress,type_places)
    #place = places[0]
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
    #details = getDetails(place,fields)

    return render_template('results.html',places=places,fields=fields,api=api)

if __name__ == "__main__":
    app.run()
