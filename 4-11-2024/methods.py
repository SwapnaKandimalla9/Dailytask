#instance method
# we are declaring adn accessing a instance variable inside a method
# while declaring instance method have to pass self as an first parameter
# we can acess these instance methods using orv or classrooms
class employee:
    def _init_(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
        def a1(self,bonus):
            self.bonus=bonus
            print(self.name)
            print(self.empid)
            print(self.salary)
            print(self.bonus)
            p = person("swapna",26,40000,5000)
            p.m1(5000)


            class Fruit:
    def __init__(self, name, color):
        self.name = name   
        self.color = color 

    def description(self):
        print(f"This is a {self.name}, and its color is {self.color}.")

    def is_ripe(self):
        if self.color.lower() == 'red':
            print(f"The {self.name} is ripe.")
        else:
            print(f"The {self.name} is not ripe yet.")

apple = Fruit("Apple", "Red")
banana = Fruit("Banana", "Yellow")

apple.description()
apple.is_ripe()       

banana.description()  
banana.is_ripe()      


#class method
#inside the class method have to use only static varible 
#while declaring classmethod have to pass @classmethod while declaring class method have to pass cls as a first 
#parameter
#using cls keyword we can declare and can acess the data inside class method.
class car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
        #@classmethod
        def m1(cls):
            car.type=sedancar
            cls.seater=4
            print(cls.model)
            print (cls.brand)
            print(car.model)
            print(cls.seater)
            c= car()
            p= m1("AudiA8",Audi)
            #static method
            class test:
                year = "2024"
                #classmethod
                def m1(cls,model):
                    print(model)
                    print(cls.year)
                    t= test()
                    t= m1("AudiA8")
                    t.m1("AudiA8")




                    class Temple:
    temple_count = 0

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Temple.temple_count += 1

    def description(self):
        print(f"The {self.name} temple is located in {self.location}.")

    @classmethod
    def get_temple_count(cls):
        print(f"Total number of temples: {cls.temple_count}")
temple1 = Temple("Golden Temple", "Amritsar")
temple2 = Temple("Kashi Vishwanath", "Varanasi")
temple3 = Temple("Tirupati Temple", "Tirumala")

temple1.description()  

Temple.get_temple_count() 


#static method
#we are not using instance and static variable
#we are not passing any parameters like self ,cls
#have to pass @static method decarator
# we can acess static method using classname and cls variable

class MathOperations:
    
    @staticmethod
    def square(number):
        return number * number

result = MathOperations.square(5)
print ({result})  



class Utility:
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

email = "user@example.com"
if Utility.is_valid_email(email):
    print(f"{email} is a valid email.")  
else:
    print(f"{email} is not a valid email.")



    class Logger:
    
    @staticmethod
    def log(message):
        print(f"[LOG]: {message}")

Logger.log("Application started")  
Logger.log("Error occurred")       




                

