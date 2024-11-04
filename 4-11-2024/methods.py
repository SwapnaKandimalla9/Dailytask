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
                

