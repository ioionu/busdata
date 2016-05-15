#!/usr/bin/env python
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus
import base64
import json
#import config
import os

def getBusGeoJSON():
    # Create your consumer with the proper key/secret.
    key=os.environ['oauthkey'] #config.key
    secret=os.environ['oauthsecret'] #config.secret

    base64string = base64.encodestring('%s:%s' % (key, secret)).replace('\n','')
    authheader =  "Basic %s" % base64string

    token_url = "https://api.transport.nsw.gov.au/auth/oauth/v2/token"

    values = dict(grant_type="client_credentials", scope="user")
    data = urlencode(values)
    req = Request(token_url, data)
    req.add_header("Authorization", authheader)

    rsp = urlopen(req)
    auth_str = rsp.read()
    auth = json.loads(auth_str)
    #print(auth['access_token'])

    from google.transit import gtfs_realtime_pb2

    url = 'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/buses'
    headers = { 'Authorization':'Bearer {}'.format(auth['access_token'])  }
    request = Request(url, headers=headers)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    #print(response_body)


    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(response_body)
    features = []

    for entity in feed.entity:
    #  if entity.HasField('trip_update'):
        #print( entity.id, entity.vehicle.position.latitude, entity.vehicle.position.longitude )
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    entity.vehicle.position.longitude,
                    entity.vehicle.position.latitude
                ]
            }
        }
        features.append(feature)
    #print response_body
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }

    return(geojson)

def test():
    return({"derp":"derp"})

if __name__ == "__main__":
    print(getBusGeoJSON())
