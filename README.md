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

Further testing has revealed a problem with the use of np.floor_divide(). When calculating the factorial-digits for 100 the answer is 645 rather than 648. For this reason the "//" operator in python was rather used.

The numpy library has problems with its floating point precision even though number is always kept at int.

