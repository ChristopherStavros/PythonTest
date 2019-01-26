from movie import Movie

class User:
    #set parameters for object
    def __init__(self, name):
        self.name = name
        self.movies = []

    # define a string that represents the object
    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre): # my_user_object.add_movie("name", "genre")
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        #self.movies = [movie for movie in self.movies if movie.name!=name]
        self.movies = list(filter(lambda movie: movie.name!=name, self.movies))
    
    def watched_movies(self):
        #return [m for m in self.movies if m.watched == True]
        return list(filter(lambda movie: movie.watched, self.movies))

    def set_watched(self,name):
        for movie in self.movies:
            if name == movie.name:
                movie.watched=True

    def json(self):
        return {
            'name' : self.name,
            'movies' : [
                movie.json() for movie in self.movies
            ] 
        }

    @classmethod
    def from_json(cls, json_data):
        user = cls(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies
        return user

