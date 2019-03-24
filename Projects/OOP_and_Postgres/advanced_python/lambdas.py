# Takes in a paramter x and returns whether x is greate than 5
l = lambda x : x > 5

print(l(10))

''' same
def l(x):
    return x > 5
print(l(10))
'''

def alter(values, check):
    #return list(filter(check, values))   # SAME
    return [val for val in values if check(val)] # this is more pythonic than filter method

my_list = [1,2,3,4,5]
another_list = alter(my_list, lambda x: x!=5)
print(another_list)

'''same
def check_not_five(x):
    return x != 5
another_list = alter(my_list, check_not_five)
print(another_list)
'''

def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

def skip_letter(value, letter):
    return alter(value, lambda x: x != letter )

print(remove_numbers("hell5lo"))
print(skip_letter("hello", "e"))