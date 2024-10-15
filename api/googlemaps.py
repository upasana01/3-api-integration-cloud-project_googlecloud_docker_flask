import requests
from geopy.distance import geodesic
import os

def check_book_availability_nearby(latitude, longitude, radius=5000):
    location = f'{latitude},{longitude}'
    isbn = '9780451524935'  # Example ISBN
    #api_key = 'AIzaSyBXQ6GPOx7pihw4TR4lF6m-pxGUNmuUm0k'  # Replace with your actual API key
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'type': 'book_store',
        'keyword': isbn,
        'key': api_key
    }

    response = requests.get(endpoint_url, params=params)
    if response.status_code != 200:
        return "Error: API request unsuccessful. Status code: {}".format(response.status_code)

    results = response.json().get('results', [])
    filtered_results = []

    for place in results:
        place_location = (place['geometry']['location']['lat'], place['geometry']['location']['lng'])
        distance = geodesic((latitude, longitude), place_location).meters
        if distance <= radius:
            filtered_results.append(place)

    if not filtered_results:
        return "No book stores found nearby within the specified radius."

    google_maps_url = "https://www.google.com/maps/dir/?api=1&destination=bookstores near {}".format(location)
    for place in filtered_results:
        lat, lng = place['geometry']['location']['lat'], place['geometry']['location']['lng']
        google_maps_url += "&waypoints={},{}".format(lat, lng)

    print(google_maps_url)
    return google_maps_url