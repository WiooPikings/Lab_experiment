
# importing the module 
import numpy as np 
  
# creating a NumPy array 
complex_num = np.array([-1 + 9j, 2 - 77j, 
                        31 - 25j, 40 - 311j, 
                        72 + 11j]) 
  
# traversing the list 
for i in range(len(complex_num)): 
      print("{}. complex number is {}".format(i + 1, complex_num[i])) 
      print ("The real part is: {}".format(complex_num[i].real)) 
      print ("The imaginary part is: {}\n".format(complex_num[i].imag)) 

  
# creating a NumPy array 
complex_num = np.array([-1, 31, 0.5]) 
  
# traversing the list 
for i in range(len(complex_num)): 
      print("{}. Number is {}".format(i + 1, complex_num[i])) 
      print ("The real part is: {}".format(complex_num[i].real)) 
      print ("The imaginary part is: {}\n".format(complex_num[i].imag)) 

import cmath
a = 2+4j
Res = cmath.polar(a)
print(Res)  # Output(4.47213595499958, 1.1071487177940904)

Res1 = cmath.phase(a)
print(Res1)

Res2 = cmath.rect(4.47213595499958, 1.1071487177940904)
print(Res2) # Output = (2.0000000000000004+4j)

a = 2+4j
p = cmath.phase(a)
print(cmath.sin(p)) # Output = (0.8944271909999159+0j)

print(cmath.exp(a))
# Output = (-1.1312043837568135+2.4717266720048188j)

a = 1+2j
print(cmath.log10(a))
#  Output (0.3494850021680094+0.480828578784234j)

print(cmath.sqrt(a))
