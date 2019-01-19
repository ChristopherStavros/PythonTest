from user import User
import json

# Instantiate object
user = User("Hans Gruber")

#  Append movie object to user.movies list
user.add_movie("Die Hard", "Action")
user.add_movie("Die Hard 3", "Action")

print(user.json())

with open('my_file.json', 'w') as f:
    json.dump(user.json(), f)
    