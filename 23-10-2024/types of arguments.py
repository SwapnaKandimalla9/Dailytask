"""
types of arguments:-
positional arguments
keyword arguments
variable length keyword arguments
default arguments"""

#***1.positional arguments: these are the arguments which are passed to a function in a correct positional order
#the total number arguments used in a function should be equal to arguments used in function definition
# if they are not equal then the function return a type error

#example program:
def add (a,b):
    return a + b 

print(add(10,20))
print(add(20,10))

#***2.default arguments:these are the arguments for which default values are assigned during function declaration
# these  values are used only when the value of such arguments are not provided in the function call

## example program 
"""def greet("Hi", none):
    print(Hi + " " none)
    greeting = input()
    name = input()
    greet()
    """
#***3. keyword arguments:-these are the arguments which are identified by the caller of the function
#using thier parameter names
# it allows the caller of the function to specify only two arguments and in any order
#example program
def add (x, y= 20,z = 30):
    sum = x+y+z
    print(sum)
    add(10,20,30)==30
    add(10, y = 40)==80
    add(10,z= 20)==50

    #**3.varible length or orbitary orguments:-these are the arguments where length is not known before runtime
    # or even during execution are reffered to as variable length arguments
    # we can pass any number of values
    ## program
    def wish(*no):
        print(no)
        wish(10,20,30,40)
        





