
import os
import sys
import numpy as np

# Read argument passed in docker run command
number=sys.argv[1]

# Test whether argument is number
if number.isdigit():
    # cast to int for factorial
    number=int(number)

    # Compute factorial
    fact=np.math.factorial(number)

    total=0
    while fact>0:
        total=total+np.mod(fact,10)     # Shift right digits through mod 10
        fact=fact//10   # Get rid of remainders

    print(total)
    
else:
    print("Enter a positive integer")

