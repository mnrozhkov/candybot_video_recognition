import urllib.parse, urllib.request
import json

google_geolocation_api_key = 'AIzaSyDHoQ998wGEozdEZOz2QaOH1sKmfDFRdK8'
google_geocoding_api_key = 'AIzaSyBISByFkDhA4kIYf4ZrkprihC47ZGGfEUo'
google_place_api_key = 'AIzaSyCJ7BtaCfAK96HOIjN2rBG0wc2uvOpx7wE'


def get_coordinates(country_code=8, mobile_network_code=None, radio_type='gsm',
                    provider=None, geoloc_ip='true'):
    '''Get location coordinates
    Args:
        country_code: international country code
        mobile_network_code: local network code
        radioType: radio broadcasting standard type
        provider: mobile net provider
        geoloc_ip: geolocation by IP-address
    Returns:
        [lat,lng,accuracy]: coordinates and accuracy if data recieved
        None: if exception caught
    '''
    
    global google_geolocation_api_key
    
    url  = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + google_geolocation_api_key
    header = {"Content-Type":"application/octet-stream"}
    data = {'homeMobileCountryCode': country_code,
            'homeMobileNetworkCode': mobile_network_code,
            'radioType': radio_type,
            'carrier': provider,
            'considerIp': geoloc_ip,
            'cellTowers': [],
            'wifiAccessPoints': []}
    params = json.dumps(data).encode('utf8')
    try:
        req = urllib.request.Request(url, data=params,
                                 headers={'content-type': 'application/json'})
        response = urllib.request.urlopen(req)
        json_response = json.loads(response.read().decode('utf-8'))
        return [json_response['location']['lat'], json_response['location']['lng'],
                json_response['accuracy']]
    except:
        return None

        
def get_address_info(address):
    '''Gets geografic information by address
    Args:
        address: place address in free string representation
    Reutrns:
        json information representation: if data recieved
        None: if exception caught
    '''
    
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    url += urllib.parse.quote(address) + '&language=ru&key=' + google_geocoding_api_key
    try:
        response = urllib.request.urlopen(url)
        json_response = json.loads(response.read().decode('utf-8'))
        return json_response
    except:
        return None

def get_near_ojects(location, radius=500):
    '''Gets geografic information by address
    Args:
        location=[lat,lng]: place location
        radius: searching nearest objects radius
    Reutrns:
        json information representation: if data recieved
        None: if exception caught
    '''
    
    if radius > 50000:
        radius = 50000
    
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    url += str(location[0]) + ',' + str(location[1]) + '&radius=' + str(radius)
    url += '&language=ru&key=' + google_place_api_key
    try:
        response = urllib.request.urlopen(url)
        json_response = json.loads(response.read().decode('utf-8'))
        return json_response
    except:
        return None
