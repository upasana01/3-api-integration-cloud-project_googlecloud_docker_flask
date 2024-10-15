# open_library.py
import requests

def search_books_by_genre(genre, limit=100):
    url = "https://openlibrary.org/search.json"
    params = {"q": genre, "limit": limit}
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None
