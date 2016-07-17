import fresh_tomatoes
import movie
import json

movies = []

with open('movies.json') as data_file:    
    for mData in json.load(data_file):
        movies.append(movie.Movie(mData['title'], mData['trailer'], mData['image']))

fresh_tomatoes.open_movies_page(movies)
