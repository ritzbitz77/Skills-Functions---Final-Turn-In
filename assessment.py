# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_total_price(default_tax, state, cost):
    """ Calculuate total price give tax amount, state and cost

    The default tax for all states excluding CA is 5%, CA is 7%, no response defaults 5% """
    
    default_tax = .05

    if state == "CA":
        default_tax = .07

    elif state == " ":
        default_tax = .05

    total_price = cost * (default_tax + 1)

    return total_price

print calculate_total_price(.05, "CA", 12)



#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

def is_berry(fruit_name):
    """ This function will return a boolean of T/F depending on the type of berry."""
    
    if fruit_name == "strawberry":
        return True
    elif fruit_name == "blackberry":
        return True
    elif fruit_name == "cherry":
        return True
    else:
        return False



def shipping_cost(fruit_name):
    """This function returns a 0 or 5 depending if fruit name is a berry."""
    if is_berry(fruit_name):
        return 0
    else:
        return 5

print is_berry("cherry")
print shipping_cost("apple")



def is_hometown(town_name):
    ''' This function determines if the town name is my home town'''

    if town_name == "Silver Spring":
        return True
    else:
        return False

print is_hometown("Gaithersburg")



def full_name(first_name, last_name):
    '''This function will return a full name combining first and last names.'''

    return first_name + " " + last_name

print full_name("Ritu", "Virmani")



def hometown_greeting(home_town, first_name, last_name):
    '''This function returns a greeting depending on whether person is from hometown or not.'''

    if is_hometown(home_town):
        return "Hi, %s, we're from the same place!" % (full_name(first_name, last_name))
    else:
        return "Hi  %s', where are you from?" % (full_name(first_name, last_name))

print hometown_greeting("Silver Spring", "Ritu", "Virmani")
print hometown_greeting("Germantown", "Ritu", "Virmani")

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def increment(x = 1):
'''This function creates a function that takes an argument and adds it to the outer functions argument.'''

    def add(y):
        return x + y
    
    return add

addfive = increment(x = 5)

print addfive(y = 5)
print addfive(y = 20)

def awesome_digits(number, list_of_numbers):

    list_of_numbers.append(number)
    return list_of_numbers


print awesome_digits(5, [7, 4, 5, 2])





#####################################################################