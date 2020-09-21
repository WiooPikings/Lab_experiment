# if Statements
'''
Perhaps the most well-known statement type is the if statement. For example:'''

x = int(input("Please enter an integer: "))
# Output = Please enter an integer: 42
if x < 0:
	x = 0
	 print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('Grater than one')


# Python for Statements
# Measure some strings:
 words = ['cat', 'window', 'defenestrate']
 for w in words:
	print(w, len(w))
# Output
cat 3
window 6
defenestrate 12

'''Code that modifies a collection while iterating over that same collection can be tricky to get right.
Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:'''

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val
print("The sum is", sum) # Output : The sum is 48

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])
# Output: I like pop
	# I like rock
	# I like jazz
	
# Python while statement

# The general syntax for the while statement looks like this:
Data = []
prompt = "What is the meaning of life, the universe, and everything? "

while number != "exit":
   Data.append(input(prompt))
   print(Data)
	
