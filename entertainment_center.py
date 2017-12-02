import fresh_tomatoes
import media
import urllib
import json
import re
import tmdbsimple as tmdb
from unidecode import unidecode


''' file create movies to be loaded from an instance of Media class '''

    #method to convert movie name to snake case https://stackoverflow.com/a/1176023/851056
def convert(name):
    new_name = name.replace(" ", "").replace("'","")
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', new_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    
def remove_non_ascii(text):
    return text.encode("utf-8")
    
    # For call to str(). Prints readable form
def __str__(input):
    return '%s' % (input)

list_of_movies = ["The Devil's Advocate", "Inception",  "Alfie", "Everything's Gone Green", "American Hustle", "Lord of The Rings"]
tmdb.API_KEY = 'a2c2494f6db6d934edc2563b347047bb'
search = tmdb.Search()
response = search.movie(query="Inception")
# print (search.results)
# print response
# i = 1
j = 0
count = len(list_of_movies)
convert(list_of_movies[j])
build_movies = []
             

while j < count :

        search = tmdb.Search()
        response = search.movie(query=list_of_movies[j])

        s = search.results[0]
        
        movie_name = convert(list_of_movies[j])
        video = "https://www.youtube.com/watch?v=bu8Gtbljw4E"
        title =  list_of_movies[j]
        poster_image_url =  'http://cf2.imgobject.com/t/p/original' + s['poster_path']
        trailer_youtube_url =  video
        
        i = media.Movies(remove_non_ascii(title), remove_non_ascii(poster_image_url), remove_non_ascii(trailer_youtube_url))
        print i #out puts as it should
        build_movies.append(i)


        j += 1

print build_movies #outputs with extra quotation marks which causes method below to throw an error
fresh_tomatoes.open_movies_page(build_movies)
