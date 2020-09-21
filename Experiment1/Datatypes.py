# Python Integers and Floating Point

type(5) # Output int
type(5.0) # Output float

# Python Strings

String_data = 'Abcdefghijk'
type(String_data) # Output str
print(String_data[::]) # Output : Abcdefghijk
print(String_data[::2]) # OP : Acegik
print(String_data[0:3]) # OP : Abc
print(String_data[::-1]) # OP : kjihgfedcbA


# Python List

a = [5,10,15,20,25,30,35,40]
# a[2] = 15
print("a[2] = ", a[2])
# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])
# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])



# Python Tuple
t = (5,'program', 1+3j)
# t[1] = 'program'
print("t[1] = ", t[1])
# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10

# Python Set
a = {5,2,3,1,4}
# printing set variable
print("a = ", a)
# data type of variable a
print(type(a))

# Python Dictionary

d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);
# Generates error
print("d[2] = ", d[2]);

# Conversion between data types
int(10.6)
#Output = 10
 int(-10.6)
#Output=-10
float(5)
# Output= 5.0
set([1,2,3])
# Output = {1, 2, 3}
tuple({5,6,7})
# Output = (5, 6, 7)
list('hello')
# Output = ['h', 'e', 'l', 'l', 'o']
dict([[1,2],[3,4]])
# Output = {1: 2, 3: 4}
dict([(3,26),(4,44)])
# Output = {3: 26, 4: 44}

