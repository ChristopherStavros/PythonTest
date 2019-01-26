from user import User 

my_user = User('Queezy@steezcorp', 'Queezy', 'McSteezy', None)
my_user.save_to_db()

my_user = User('steez@steezcorp', 'Steez', 'Mcqueez', None)
my_user.save_to_db()

my_user = User.load_from_db_by_email('Queezy@steezcorp')
print(my_user)
