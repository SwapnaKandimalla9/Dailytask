""""""
python modules:module - it is used for storing the data and passing the data one module to another
    module for redability of Code 
modules are two types:-
1.customized modules
built in module 
1. customized module is created by developers
ex:-module_1,module_2
2.built in module means it is already exsisting in python
ex:-math,random,datetime etc...

##here we are creating module-1 as customized module
from module_1 import mul, add,even-nums

x = 10
y = 30
print(add(x,y))

print(mul(x,y))

x = [1,2,3,4,5,6,7,8,9,10]
print(even_nums(x))

#examples of built-in modules:-

# functool module:-which is included in pythons standatd liabrary,
#provides essesntial functionality for working with high-order functiond

from functools import reduce
list1 = [2,4,7,9,1,3]
sum-of-list1 = reduce(lambda a, b:a if a>b else b,list2)

print('sum of list1 :', sum of_list1)
print('maximum of list2 :', max_of_list2)

#random module:- the random module in python is used to generates random numbers
# and provides the functionality of various random operations such as 'random.randint()',
#'random.choice()','random.random()','random.shuffle()'and many more.

import random
num = random.randint(1,10)
print("random integer between 1 and 10 :{num}")

fruits = ["apple","mango","kiwi","orange","grapes"]
choose_fruit = random.choice(fruits)
print("randomly chosen language: {choosen_fruit}")

#datetime module:- the datetime module allows for manipulation and reading of date and time values.
# some of the basic method of "datetime"module are "datetime.date","datetime.time".
"datetime.datetime",and "datetime.timedeta".

impoer datetime
pront (dir(datetime))
print(datetime.time(12,50,30))
print9datetime.datetime(2024,11,19)
