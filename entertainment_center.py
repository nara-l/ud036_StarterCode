import fresh_tomatoes
import media
import urllib
import json
import re
import tmdbsimple as tmdb

''' file create movies to be loaded from an instance of Media class '''

#method to convert movie name to snake case https://stackoverflow.com/a/1176023/851056
def convert(name):
    new_name = name.replace(" ", "").replace("'","")
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', new_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

# Create objects of Class Movie for the different movies we wish to display

alfie = media.Movies("Alfie",
                "http://www.gstatic.com/tv/thumb/movieposters/34949/p34949_p_v8_aa.jpg",
                "https://www.youtube.com/watch?v=T-whOtC8aak")

inception = media.Movies("Inception",
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
                                "https://www.youtube.com/watch?v=66TuSJo4dZM")

midnight_in_paris = media.Movies("Mid Night in Paris",
                                "http://is5.mzstatic.com/image/thumb/Video/v4/80/5c/8f/805c8f2a-5d93-0621-2f3d-2f23ba60f775/source/1200x630bb.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

lord_of_the_rings = media.Movies("Lord of The Rings",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi00MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                                "https://www.youtube.com/watch?v=Pki6jbSbXIY")
        
devils_advocate = media.Movies("The Devil's Advocate",
                                "http://www.gstatic.com/tv/thumb/movieposters/19989/p19989_p_v8_af.jpg",
                                "https://www.youtube.com/watch?v=40hHA9n4C2o")
        
everythings_gone_green = media.Movies("Everything's Gone Green",
                                "http://www.gstatic.com/tv/thumb/dvdboxart/163232/p163232_d_v8_aa.jpg",
                                "https://www.youtube.com/watch?v=bu8Gtbljw4E")

#movies_json = urllib.urlopen('http://www.omdbapi.com/?t=inception&apikey=da89c944')
#mjson = movies_json.read()
#mdata = json.loads(mjson)
#movies_json.close()
#print (mdata) #Plot, Title #Poster

# Populate the list of movies for input to the open_movies_page

#movies_ = [alfie, inception, midnight_in_paris, lord_of_the_rings, devils_advocate, everythings_gone_green]
#fresh_tomatoes.open_movies_page(movies)
list_of_movies = ["The Devil's Advocate", "Inception",  "Alfie", "Everything's Gone Green", "American Hustle", "Lord of The Rings"]
tmdb.API_KEY = 'a2c2494f6db6d934edc2563b347047bb'
search = tmdb.Search()
response = search.movie(query="Inception")
print (search.results)
#print response
i = 1
j = 0
count = len(list_of_movies)
convert(list_of_movies[j]) 
build_movies = []
x_loop_must_break = False
'''
while j < count :
       
        search = tmdb.Search()
        response = search.movie(query=list_of_movies[j])
        print (search.results)
        for s in search.results:
                #print(s['title'], s['id'], s['poster_path'])
                movie_name = convert(list_of_movies[j])
                video = "https://www.youtube.com/watch?v=bu8Gtbljw4E"

                title =  '"' + list_of_movies[j] +  '"'
                poster_image_url =  '"' + 'http://cf2.imgobject.com/t/p/original' + s['poster_path'] +  '"'
                trailer_youtube_url =  '"' + video +  '"'

                movie_name =   media.Movies(title, poster_image_url, trailer_youtube_url)
                #print title + poster_image_url + trailer_youtube_url
                build_movies = [list_of_movies[j]]
                # Want just first result. Could not read just first item of json by search.results[0]
                if(i==1):
                        x_loop_must_break = True
                        break
        if x_loop_must_break: break

        j += 1

#print build_movies 
'''
