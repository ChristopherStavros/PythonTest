from database import Database
from user import User

login = {
    'host' : "localhost",  
    'database' : "learning", 
    'user' : "postgres", 
    'password' : "P@ssw0rd"
}

Database.initialise(**login)

my_user = User('jackson@steezcorp.com', 'Action', 'Jackson', None)
my_user.save_to_db()

# my_user = User('steez@steezcorp.com', 'Steez', 'Mcqueez', None)
# my_user.save_to_db()

my_user = User.load_from_db_by_email('jackson@steezcorp.com')
print(my_user)
