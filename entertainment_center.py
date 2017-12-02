import fresh_tomatoes
import media
import re
import tmdbsimple as tmdb
from unidecode import unidecode


''' File create movies to be loaded from an instance of Media class.
     Movie details are from TMDB api '''


def remove_non_ascii(text):
    return text.encode("utf-8")


# create list of movies here. Add as many as you wish
list_of_movies = ["The Devil's Advocate", "Inception", "Alfie",
                  "Temple Grandin", "American Hustle",
                  "Lord of The Rings", "Death Note",
                  "Batman Begins", "Gone Girl"]

# start using tmdb api
tmdb.API_KEY = 'a2c2494f6db6d934edc2563b347047bb'
j = 0
count = len(list_of_movies)
build_movies = []

while j < count:

    search = tmdb.Search()
    response = search.movie(query=list_of_movies[j])
    s = search.results[0]

    ''' get youtube trailers at once without making
        a second call https://github.com/celiao/tmdbsimple/issues/6
    '''
    kwargs = {'append_to_response': 'trailers'}
    movie_ = tmdb.Movies(s['id']).info(**kwargs)
    video_ = movie_.get('trailers')

    # to eliminate indexError
    for index, value in enumerate(video_['youtube']):
        if value is not 0:
            vid_source = video_['youtube'][index]['source']

    # get variables needed for media class
    trailer_youtube_url = "https://www.youtube.com/watch?v=" + vid_source
    title = list_of_movies[j]
    poster_image_url = 'http://cf2.imgobject.com/t/p/original' + \
        s['poster_path']

    # create an instance of media class for every movie
    i = media.Movies(remove_non_ascii(title), remove_non_ascii(
        poster_image_url), remove_non_ascii(trailer_youtube_url))

    # populate list for fresh tomatoes
    build_movies.append(i)

    j += 1

# print build_movies

# render page
fresh_tomatoes.open_movies_page(build_movies)
