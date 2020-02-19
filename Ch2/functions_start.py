#
# Example file for working with functions
#

# define a basic function
def someFunction():
    print("Some function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1 + arg2)

# function that returns a value
def area(l,b):
    print(l*b)

# function with default value for an argument
def func3(num,x=1):
    result=1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def func4(*args):
    result=0
    for i in args:
        result += i
    return result

# someFunction()
# print(someFunction())
# someFunction

# func2(2,5)
# area(4,5)
# print(func3(4))
# print(func3(3,4))
# print(func3(x=5, num=2))
print(func4(2,3,6))