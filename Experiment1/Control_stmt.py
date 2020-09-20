# if Statements
'''
Perhaps the most well-known statement type is the if statement. For example:'''

	>>> x = int(input("Please enter an integer: "))
	Please enter an integer: 42
	>>> if x < 0:
	...     x = 0
	...     print('Negative changed to zero')
	... elif x == 0:
	...     print('Zero')
	... elif x == 1:
	...     print('Single')
	... else:
	...     print('More')
	...
'''There can be zero or more elif parts, and the else part is optional.
 The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
  An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.'''

# Python for Statements
'''
The for statement in Python differs a bit from what you may be used to in C or Pascal.
 Rather than always iterating over an arithmetic progression of numbers (like in Pascal),
  or giving the user the ability to define both the iteration step and halting condition (as C),
   Python’s for statement iterates over the items of any sequence (a list or a string),
    in the order that they appear in the sequence. For example (no pun intended):
'''

	# Measure some strings:
	>>> words = ['cat', 'window', 'defenestrate']
	>>> for w in words:
	...     print(w, len(w))
	...
	# Output
	cat 3
	window 6
	defenestrate 12

'''Code that modifies a collection while iterating over that same collection can be tricky to get right.
Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:'''

	# Strategy:  Iterate over a copy
	for user, status in users.copy().items():
	    if status == 'inactive':
	        del users[user]

	# Strategy:  Create a new collection
	active_users = {}
	for user, status in users.items():
	    if status == 'active':
	        active_users[user] = status

# Python while statement

# The general syntax for the while statement looks like this:
	number = 0
	prompt = "What is the meaning of life, the universe, and everything? "

	while number != "42":
	    number =  input(prompt)

# Applications of Whlie
	name = 'Harrison'
	guess = input("So I'm thinking of person's name. Try to guess it: ")
	pos = 0

	while guess != name and pos < len(name):
	    print("Nope, that's not it! Hint: letter ", end='')
	    print(pos + 1, "is", name[pos] + ". ", end='')
	    guess = input("Guess again: ")
	    pos = pos + 1

	if pos == len(name) and name != guess:
	    print("Too bad, you couldn't get it.  The name was", name + ".")
	else:
	    print("\nGreat, you got it in", pos + 1,  "guesses!")
	    
'''The flow of execution for a while statement works like this:

    Evaluate the condition (BOOLEAN EXPRESSION), yielding False or True.
    If the condition is false, exit the while statement and continue execution at the next statement.
    If the condition is true, execute each of the STATEMENTS in the body and then go back to step 1.

The body consists of all of the statements below the header with the same indentation.

The body of the loop should change the value of one or more variables so that eventually the condition becomes false and the loop terminates.
Otherwise the loop will repeat forever, which is called an infinite loop.'''
