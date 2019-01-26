'''
User can pick six numbers
Lotter calculates 6 random number (between 1 and 20)
Then we match the user numbers ti the lottery numbers
Calculate the winnings based on how many numbers the user matched
'''
import random

def menu():
    #Ask the player for numbers
    player_numbers = get_player_numbers()

    # Calculate the lottery numbers
    lottery_numbers = create_lottery_numbers()
    print(lottery_numbers)
    
    # Print out the winnings
    matching_numbers = player_numbers.intersection(lottery_numbers)
    print("You matched {}.  You won ${}!".format(matching_numbers, 100 ** len(matching_numbers)))
    

# User can pick 6 numbers
def get_player_numbers():
    #Get user input string
    number_csv = input("Enter six numbers sepated by commas: ")
  
    # Convert string to list and strip out commas
    number_list = number_csv.split(',')

    # Convert strings to ints and build a set
    integer_set = {int(number) for number in number_list}
    return integer_set

# Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()

    while len(values) < 6:
        values.add(random.randint(1,20))

    return values

#Main program
menu()
