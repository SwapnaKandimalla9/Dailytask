
"""
inheritence:-
        it inherits the properties from parent class to the child class.

types of inheritence:-
1.sigle inheritence:-  a child class inherits properties and methods from a single parent class.

2.multiple inheritence:- a class to inherit attributes and methods from more than one parent class.

3.hierachical inheritence:- inheriting properties and method from single class from multiple class at a same time.

4.multilevel inheritence:- inheriting properties from multilevel clases to single class.

5.hybrid inheritence:- using more then one type of inheritence.
"""

#example of single inheritence

# Parent class: GroceryItem
class GroceryItem:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_item_details(self):
        print(f"Item: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price per unit: ${self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Price: ${self.price * self.quantity}")

# Child class: Fruit inheriting from GroceryItem
class Fruit(GroceryItem):
    def __init__(self, name, price, quantity, color, is_organic):
        # Call the constructor of the parent class
        super().__init__(name, "Fruit", price, quantity)
        self.color = color          # Color of the fruit (e.g., red, green, yellow)
        self.is_organic = is_organic  # Whether the fruit is organic or not

    def display_fruit_details(self):
        self.display_item_details()  # Call the parent method to display common details
        print(f"Color: {self.color}")
        print(f"Organic: {'Yes' if self.is_organic else 'No'}")

# Creating a GroceryItem instance
grocery_item = GroceryItem("Rice", "Grain", 2.50, 3)
print("Grocery Item Details:")
grocery_item.display_item_details()

print("\n" + "-"*50 + "\n")

# Creating a Fruit instance
fruit = Fruit("Apple", 1.20, 5, "Red", True)
print("Fruit Details:")
fruit.display_fruit_details()



#example of multiple inheritence:-
# Parent class: Flyable
class Flyable:
    def fly(self):
        print("Flying in the sky.")

# Parent class: Swimmable
class Swimmable:
    def swim(self):
        print("Swimming in the water.")

# Child class: FlyingFish (Multiple Inheritance)
class FlyingFish(Flyable, Swimmable):
    def action(self):
        self.fly()   # Using Flyable's method
        self.swim()  # Using Swimmable's method

# Creating an instance of FlyingFish
fish = FlyingFish()
fish.action()


#example of multilevel inheritence

class GF:
        def m1(self):
                self.car = "BMW"
class F(GF):
        def m2(self):
               print(self.car)
               self.car = "RANGE ROVER"
class C(F):
        def m3(self):
                print(self.car)
                self.car = "MAHINDRA"
                print(self.car)
c = C()
c.m1()
c.m2()
c.m3()

#example of heirachial inheritence:-
class gf:
    def __init__(self):
        self.land=20
 
class f(gf):
    def m1(self):
        print("father",self.land-10)
 
class c(gf):
    def m2(self):
        print("child",self.land-10)
 
F = f()
F.m1()
C = c()
C.m2()   


#example of hybrid inheritence:-
# Parent class: Person (Single Inheritance)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Parent class: Manager (Single Inheritance)
class Manager:
    def __init__(self, department):
        self.department = department

    def display_manager_info(self):
        print(f"Department: {self.department}")
        print(f"Role: Manager")

# Parent class: Technician (Single Inheritance)
class Technician:
    def __init__(self, skill):
        self.skill = skill

    def display_technician_info(self):
        print(f"Skill: {self.skill}")
        print(f"Role: Technician")

# Child class: HybridEmployee (Hybrid Inheritance)
class HybridEmployee(Person, Manager, Technician):
    def __init__(self, name, age, department, skill):
        # Initialize all parent classes
        Person.__init__(self, name, age)
        Manager.__init__(self, department)
        Technician.__init__(self, skill)

    def display_employee_info(self):
        # Calling methods from all parent classes
        self.display_person_info()      # From Person class
        self.display_manager_info()     # From Manager class
        self.display_technician_info()  # From Technician class

# Creating an instance of HybridEmployee
employee = HybridEmployee("swapna", 26, "IT", "Networking")
employee.display_employee_info()

