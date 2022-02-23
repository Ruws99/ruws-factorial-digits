# ruws-factorial-digits
Technical Assignment test 

Herewith follows the complete guide to this technical assignment:
 
The Python script is quite straightforward, using "numpy" to compute the factorial of a number. Afterwards mod 10 is used to shift out digits that is then summed to produce the end result. This procedure is used to adhere to the requirement to avoid casting variables.
 
The script also pre-emptively checks whether a number passed to the docker container is in fact a positive integer before proceeding with the operation.
 
The script is packaged as a docker container with the following build command:
  docker build -t factorial-digits .
  
and the run command:
  docker run --rm factorial-digits (number)
  
Please note: for the number(number) argument to be passed into Python the "sys" and "os" library is used to read the parameter as an argument. One thing to note here is that the argument is always read as a string and that casting is needed to int in order for the script to execute.


The numpy library has problems with its floating point precision even though number is always kept at int.

![image](https://user-images.githubusercontent.com/79838587/155290982-10b7ca29-08c2-4ca7-9510-3c67b11d8538.png)


As can be seen above with np.floor_divide the int is converted into a float which then meddles with the floating point precision of the operation. 

The same problem occurs with the np.mod function: 

![image](https://user-images.githubusercontent.com/79838587/155426544-5361d0ba-1622-4179-92fd-5b3136e8dfe4.png)

which is of course wrong.

The best way to deal with these problems is to use the "%" operator for mod and "//" for floor division instead of their numpy counterparts.

However, based on the assignment's instructions, all math operations is to be handled and a workaround is needed.
This is done with the Fractions library that is essentially a very accurate representation of a float type. This helps to represent the large number as a very precise floating-point number and negates the floating-point precision error encountered.




