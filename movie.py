class Movie():
    ''' Class that describes a movie '''
    def __init__(self, mTitle, mTrailer, mImage):
        ''' Constructor that sets instance variables using in parameters '''
        self.title = mTitle
        self.trailer_youtube_url = mTrailer
        self.poster_image_url = mImage
