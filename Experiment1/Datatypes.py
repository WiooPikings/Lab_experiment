# Python Integers and Floating Point

'''In python, integers and numbers with decimal are two different data types.
But in javascript, there is only one data type “number” to combine them.'''
     
     type(5) # Output int
     type(5.0) # Output float

# Python Strings

'''Both languages have ‘strings’ data type, and the syntax are same,
 you can either use single quotes or double quotes.
  Both are ordered sequences, which means we can use [] square brackets and a number index to indicate position of the character we want to grab out of the string. There is a difference here between two languages. In python, there is a reverse index of each character, while in javascript, there is no such thing.
 You can see from the below example:'''

'''Another cool function in python is the default slice method.
 Remember when I learnt javascript, if I want to find some substring of a string I need to call .slice(start, end) on the string.
  But in python, I can just use [start:end:step] square brackets to find the substring, I can even take two steps to call the substring every other character of the original one.
  There is a trick in python: remember the classic interview question about reverse string, instead of using a for loop, in python you can just call [::-1]behind the string'''

  String_data = 'Abcdefghijk'
  type(String_data) # Output str
  print(String_data[::]) # Output : Abcdefghijk
  print(String_data[::2]) # OP : Acegik
  print(String_data[0:3]) # OP : Abc
  print(String_data[::-1]) # OP : kjihgfedcbA


# Python List
'''List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ]'''

	a = [5,10,15,20,25,30,35,40]

	# a[2] = 15
	print("a[2] = ", a[2])

	# a[0:3] = [5, 10, 15]
	print("a[0:3] = ", a[0:3])

	# a[5:] = [30, 35, 40]
	print("a[5:] = ", a[5:])



# Python Tuple

'''Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

It is defined within parentheses () where items are separated by commas.'''

	t = (5,'program', 1+3j)

	# t[1] = 'program'
	print("t[1] = ", t[1])

	# t[0:3] = (5, 'program', (1+3j))
	print("t[0:3] = ", t[0:3])

	# Generates error
	# Tuples are immutable
	t[0] = 10

# Python Set

'''
Set is an unordered collection of unique items.
 Set is defined by values separated by comma inside braces { }.
  Items in a set are not ordered.
'''

	a = {5,2,3,1,4}

	# printing set variable
	print("a = ", a)

	# data type of variable a
	print(type(a))

# Python Dictionary

'''Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data.
 Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.
In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.'''

	d = {1:'value','key':2}
	print(type(d))

	print("d[1] = ", d[1]);

	print("d['key'] = ", d['key']);

	# Generates error
	print("d[2] = ", d[2]);

# Conversion between data types

'''
We can convert between different data types by using different type conversion functions like int(), float(), str(), etc.'''
	>>> int(10.6)
	10
	>>> int(-10.6)
	-10
	>>> float(5)
		5.0
	>>> set([1,2,3])
	{1, 2, 3}
	>>> tuple({5,6,7})
	(5, 6, 7)
	>>> list('hello')
	['h', 'e', 'l', 'l', 'o']
	>>> dict([[1,2],[3,4]])
	{1: 2, 3: 4}
	>>> dict([(3,26),(4,44)])
	{3: 26, 4: 44}

