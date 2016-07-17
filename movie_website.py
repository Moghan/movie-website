import fresh_tomatoes
import movie
import json

# List for storing movies
movies = []

# Open file and append movies found to the movies list
with open('movies.json') as data_file:    
    for mData in json.load(data_file):
        movies.append(movie.Movie(mData['title'], mData['trailer'], mData['image']))

# external website generator with list of movies as parameter
fresh_tomatoes.open_movies_page(movies)
