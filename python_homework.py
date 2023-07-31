# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.
# def hello_name(user_name):

def hello_name(user_name):
    """Display a simple greeting."""
    print("Hello_" + user_name.upper() + "!")

hello_name('Leza')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
# def first_odds():

def first_odds():
    for number in range(1, 100):
        if number % 2 != 0:
            print(number)

# first_odds()   <---------------------- returns nothing without this line 

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.
# def max_num_in_list(a_list):

def max_num_in_list(a_list):
    max = a_list[0]
    for num in a_list:
        if num > max:
            max = num
    return max
print(max_num_in_list([4, 2, 14, -5, 10]))     # output will be 14


# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
# def is_leap_year(a_year):

def is_leap_year(a_year):
        if a_year % 4 == 0:
                return True
        if a_year % 400 == 0:
                return False
        if a_year % 100 == 0:
                return True
        else:
            return False
        
a_year = 2023
print(is_leap_year(a_year))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers,
# but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
# def is_consecutive(a_list):

# this one was a struggle for me >_< but I did my best with all the resources available to me
# plus everything I've picked up thus far and used python tutor to help me execute:

def is_consecutive(a_list):   # function takes list 'a_list' as input
    int = len(a_list)         # find out the length of the list and assign it to variable 'int' (integer)
    if int == 0 or int == 1:  # check to see whether list is empty or has 1 element,
        return False          # if either is true, then function = false
# if list has more than 1 element, function continues:
    for int in range(1, int):                  # for loop function to iterate thru list
        if a_list[int] - a_list[int - 1] != 1: # starting from 1 and goes to 'int - 1'
            return False                       # inside loop, function checks difference between a_list[int] and
    return True                                # a_list[int - 1] is NOT equal to 1, if true, then not consecutive

list1 = [6, 7, 8, 9, 10]
list2 = [6, 8, 6, 10, 12]
print(is_consecutive(list1)) # True
print(is_consecutive(list2)) # False