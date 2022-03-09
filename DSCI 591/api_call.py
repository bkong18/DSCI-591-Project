#Note: The URL has been redacted from this file as it is the private Dev server of Geocode Earth. Please retrieve your own API URL from Geocode Earth,
#or contact the team with questions

import requests
s = requests.Session() #start session
def request_geo(data):
    
    lat, lon = data['latitude'], data['longitude']
    #enter URL of Geocode.Earth associated with account
    #This URL may also need to be appended to include API Key
    #Reverence Geocode.Earth docs
    url = f'{URL HERE}?geoms=0&lat={lat}&lon={lon}&class=address&limit=1'
    response = s.get(url) #request

    response_dict = response.json() #return JSON
    return response_dict
