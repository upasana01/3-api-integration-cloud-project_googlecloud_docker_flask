from flask import render_template, request
from flask.views import MethodView
from api import googlebooks, openlibrary
import os  
class GoogleBooksSearch(MethodView):

    def get(self):
        query = request.args.get('isbn')
        # apiKey = 'AIzaSyABM17l_lT8q6OnKSAHUkUsnjCCrY4jDCc'
        apiKey = os.environ.get('GOOGLE_BOOKS_API_KEY')
        if query:
            result = googlebooks.search_books(query,apiKey)
            if(result['totalItems'] > 0):
                return render_template('thirdpage.html', books=result['items'])
            else:
                return render_template('thirdpage.html')
        return render_template('thirdpage.html')

class OpenLibrarySearch(MethodView):

    def get(self):
        genre = request.args.get('genre')
        if genre:
            result = openlibrary.search_books_by_genre(genre)
            if len(result['docs']) > 0:
                # Filter out items that do not have an 'isbn' field
                filtered_docs = [doc for doc in result['docs'] if 'isbn' in doc]

                return render_template('cards_u.html', books=filtered_docs)
            else:
                return render_template('cards_u.html')        
        return render_template('cards_u.html')