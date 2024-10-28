##packages:-a package is a directory that organizes related modules,sub-packages and other resources
#packages are used to organize code,avoding name conflicts ,code reusability.
#definition:it is a simple python file .py extensions that contains collections of functions and global 
#variables.a package is a collection of different modules with an init.py file
#creating a python package
def greet(name):
    print("hello, {name}")
    def add(a,b):
        return a + b
    from mypackage import module1,module2
    module1.greet("swapna")
    result = module2.add(3,5)
    print("the result of addition is:",result)