# google_books.py
import requests

def search_books(query, api_key):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {'q': query, 'key': api_key}
    response = requests.get(base_url, params=params)
    return response.json() if response.status_code == 200 else None
