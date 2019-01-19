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
        #for movie in self.movies:
        #    if movie.name == name:
        #        self.movies.remove(movie)
        #self.movies = [movie for movie in self.movies if movie.name!=name]
        self.movies = list(filter(lambda movie: movie.name!=name, self.movies))
    
    def watched_movies(self):
        # Iterate through list
        #return [m for m in self.movies if m.watched == True]
        return list(filter(lambda movie: movie.watched, self.movies))

    def json(self):
        return {
            'name' : self.name,
            'movies' : [
                movie.json() for movie in self.movies
            ] 
        }

        
    '''
    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{}, {}, {}\n".format(movie.name, movie.genre, movie.watched))

    # CLASS METHOD!
    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")  # ['name', 'genre', 'watched']
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2]=="True"))

            user = cls(username) # user = User(username) would also work, but not preferred 
            user.movies = movies
            return user
    '''

