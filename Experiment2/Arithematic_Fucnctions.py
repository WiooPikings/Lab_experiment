# Import math Library
import math

# Return the sine of different values
print (math.sin(0.00)) # 0.0
print (math.sin(-1.23)) # -0.9424888019316975
print (math.sin(10)) # -0.5440211108893698
print (math.sin(math.pi)) # 1.2246467991473532e-16
print (math.sin(math.pi/2))  # 1.0 

# Return the cos of different numbers
print (math.cos(0.00)) # 1.0
print (math.cos(-1.23)) # 0.3342377271245026
print (math.cos(10)) # -0.8390715290764524
print (math.cos(math.pi)) # -1.0
print (math.cos(math.pi/2)) # 6.123233995736766e-17

# Import cmath
import cmath 
# Initializing real numbers 
x = 5
y = 3 
# converting x and y into complex number 
z = complex(x,y);   
# printing real and imaginary part of complex number 
print ("The real part of complex number is : ",end="") 
print (z.real) 
print ("The imaginary part of complex number is : ",end="") 
print (z.imag) 
'''Output:

The real part of complex number is : 5.0
The imaginary part of complex number is : 3.0
'''


# Initializing real numbers 
x = -1.0
y = 0.0
# converting x and y into complex number 
z = complex(x,y);   
# printing phase of a complex number using phase() 
print ("The phase of complex number is : ",end="") 
print (cmath.phase(z))
# Output: The phase of complex number is : 3.141592653589793
