#Recursion:calling the function itself
#factorial(n)=n*factorial(n-1)
#example:
#def factorial(n)
    if n == 0
    return 1
#else:
#return n*factorial(n-1)

#lambda function: it is an anonymous function.this function can have any number of parameters but,can have just one statement
#these are one line function
#it can be defined by lambda keyword
#syntax: lambda arguments:expression

#example:
def sqare(x):
    return x **2

print(square(5))
# lambda function
square_lambda=lambda x:x**2
print(square_lambda(5))

# filter function:it is a built in function ,used to filter out the elements of an iterator
#depending on a function that test each element in the sequence to be true or not
#it return there sequence of elements for which function is true
#syntax: filter(function _name,sequence-variable)
#example program:
def get_events(1):
if 1 % 2 == 0:
    return True
else
    return False
l = [1,2,3,4,5,6,7,8,9]
f = filter(get-events,1)
print(list(f))

#Reduce(): it is used reduce a sequence of elements to a single value by processing the elements 
#according to a function supplied and it returns a single value
example program
from functools import *
l = [1,2,3,4,5,6,7,8,9]
rs = reduce(lambda x,y:x+y ,1)
print(rs)
output: 45

#map function :apply function to each element of iterable
# return iterator of result
syntax : map(function,iterator)
# example prpgram
l = [1,2,34,5]
def sqr(l):
    return l *2
m = map(sqr,1)
print(list(m))
