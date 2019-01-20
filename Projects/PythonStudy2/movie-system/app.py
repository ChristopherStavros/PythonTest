from user import User
import json, os

def menu():
    # Ask for the user's name
    name = input("Enter your name: ")

    # Check if a file exists for that user
    # If it already exists, welcome then and load their data.
    # If not, create a User object
    filename = "{}.json".format(name)

    if file_exists(filename):
        with open(filename, 'r') as f:
            try:
                json_data = json.load(f)
            except json.decoder.JSONDecodeError:
                print("Invalid JSON file")
                return
        user = User.from_json(json_data)
    else:
        user = User(name)
    
    user_input = input('''Enter:
    'a' to add a movie,
    'm' to see the list of movies,
    'w' to set a movie as watched,
    'd' to delete a movie,
    'l' to see a list of watched movies,
    's' to save,
    'q' to quit
    
    ''')

    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 'm':
            for movie in user.movies:
                print("Name: {name}, Genre: {genre}, Watched: {watched}".format(**movie.json())) # This is cool!!!
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {name}, Genre: {genre}, Watched: {watched}".format(**movie.json())) # This is cool!!!
        elif user_input == 's':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)
        elif user_input == 'q':
            return
        else:
            print("That is not a valid choice")

        user_input = input('''Enter:
        'a' to add a movie,
        'm' to see the list of movies,
        'w' to set a movie as watched,
        'd' to delete a movie,
        'l' to see a list of watched movies,
        's' to save,
        'q' to quit
        
        ''')

def file_exists(filename):
    return os.path.isfile(filename)

menu()
