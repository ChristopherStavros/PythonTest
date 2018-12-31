#Assertion error are just another kind of exception
#assert False, 'This is the error message'

market_2nd = {'ns':'green','ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():  # REMEMBER that .keys() is a dictionary function
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    #avoid the yellow, green combo!!!
    #ASSERT --> I ASSERT THAT THIS CONDITION ALWAYS HOLDS TRUE
    #don't mix assert with try catch -- if assert fails, program SHOULD crash!
    #asserts are for PROGRAMMER ERRORS, not user errors
    #they are sanity checks...that should never actually be raised
    assert 'red' in intersection.values(), "Neither light is RED!!!" + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
switchLights(market_2nd)
print(market_2nd.values())
print(market_2nd)
print(market_2nd.values())
print(market_2nd)
print(market_2nd.values())

