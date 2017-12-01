class Movies():
    ''' Class encapsulates properties of a movie '''

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        
    # For call to repr(). Prints object's information
    def __repr__(self):
        return '[%s, %s, %s]' % (self.title, self.poster_image_url, self.trailer_youtube_url)    
 
    # For call to str(). Prints readable form
    def __str__(self):
       return '[%s, %s, %s]' % (self.title, self.poster_image_url, self.trailer_youtube_url)   
       
       
    __repr__ = __str__
        