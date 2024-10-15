from flask import Flask, render_template, request,jsonify
from api.googlemaps import check_book_availability_nearby
from views import GoogleBooksSearch, OpenLibrarySearch

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('landing_page.html')

# @app.route('/nearby_bookstores')
# def nearby_bookstores():
#     latitude = request.args.get('lat')
#     longitude = request.args.get('lng')
#     check_book_availability_nearby(latitude,longitude)
#     return jsonify({'success': True})

@app.route('/nearby_bookstores')
def nearby_bookstores():
    latitude = request.args.get('lat')
    longitude = request.args.get('lng')
    
    # Call the function and get the Google Maps URL
    google_maps_url = check_book_availability_nearby(latitude, longitude)

    # Check if the response is a URL or an error message
    if google_maps_url.startswith("http"):
        return jsonify({'success': True, 'url': google_maps_url})
    else:
        # Handle error scenario
        return jsonify({'success': False, 'error': google_maps_url})


app.add_url_rule('/search_open_library', view_func=OpenLibrarySearch.as_view('search_open_library'))
app.add_url_rule('/search_google_books', view_func=GoogleBooksSearch.as_view('search_google_books'))

if __name__ == '__main__':
    app.run(debug=True)