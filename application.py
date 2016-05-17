#!/usr/bin/env python2

import bus_geojson
from flask import Flask, json, render_template
application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/bus')
def bus():
    return json.jsonify(**bus_geojson.getBusGeoJSON()) #getBusGeoJSON()

if __name__ == "__main__":
    #application.debug = True
    application.run()
