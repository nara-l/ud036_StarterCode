import fresh_tomatoes
import media

''' file create movies to be loaded from an instance of Media class '''

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

# Populate the list of movies for input to the open_movies_page

movies = [alfie, inception, midnight_in_paris, lord_of_the_rings, devils_advocate, everythings_gone_green]

fresh_tomatoes.open_movies_page(movies)
