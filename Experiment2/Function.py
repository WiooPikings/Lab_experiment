# Example of a function

def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")
    
# Fuction call
greet('Paul')   # Output : Hello, Paul. Good morning!

# Example of function with return

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
# Output : 2
print(absolute_value(-4))
# OUtput : 4

# Scope and life time of a variable
def my_func():
	x = 10
	print("Value inside function:",x)
x = 20
my_func()
print("Value outside function:",x)

'''Output:
  Value inside function: 10
  Value outside function: 20 '''
