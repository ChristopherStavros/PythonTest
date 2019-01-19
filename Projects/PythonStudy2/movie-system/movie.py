class Movie:
    #set parameters for object
    def __init__(self, name, genre, watched):
        #Define the class parameters
        self.name = name
        self.genre = genre
        self.watched = watched
    # define a string that represents the object
    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json(self):
        return {
            'name' : self.name,
            'genre' : self.genre,
            'watched' : self.watched
        }
