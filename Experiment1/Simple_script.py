# Applications of Whlie
# A simple Gussing game using python 

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

# Simple code to draw letter 'Z'
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
