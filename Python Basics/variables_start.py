# 
# Example file for variables
#

# Declare a variable and initialize it
# x=5.5
# print(x)

# # re-declaring the variable works
x='acv'
# print(x)

# # ERROR: variables of different types cannot be combined
# print('acv ' + str(5.5))

# Global vs. local variables in functions
def someFunction():
    global x
    x=5
    print(x)

someFunction()
print(x)
