# use cases of oops 
#1.WEBB DEVELOPMENT

#OOP is extensively used in frameworks like Django and Flask, where models represent database 
# tables and controllers handle user requests
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

# Example usage in a web application
user = User("swapna", "swapna@gmail.com")
post = Post("My First Post", "Hello, world!")

#2.GAME DEVELOPMENT
#OOP is ideal for modeling game elements such as characters, items, and game mechanics.

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self, other):
        # Attack logic
        print(f"{self.name} attacks {other.name}")

# Example usage
hero = Character("Hero", 100)
monster = Character("Monster", 50)
hero.attack(monster)

#3. DATA ANALYSIS AND PROCESSING
#In data science, OOP can be used to encapsulate data processing logic.

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def clean(self):
        # Cleaning logic
        pass
    
    def analyze(self):
        # Analysis logic
        return self.data.mean()

# Example usage
processor = DataProcessor(data)
processor.clean()
result = processor.analyze()

#4.MACHINE LEARNING
#OOP is used to encapsulate different machine learning models and their behaviors.

from sklearn.linear_model import LinearRegression

class MLModel:
    def __init__(self):
        self.model = LinearRegression()
    
    def train(self, X, y):
        self.model.fit(X, y)
    
    def predict(self, X):
        return self.model.predict(X)

# Example usage
model = MLModel()
model.train(X_train, y_train)
predictions = model.predict(X_test)

#5.INVENTORY MANAGEMENT SYSTEM
#Classes can represent products, inventory, and order processing.

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    
    def restock(self, amount):
        self.quantity += amount

class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, product):
        self.items[product.name] = product

# Example usage
inventory = Inventory()
item = Product("Apples", 50)
inventory.add_item(item)
item.restock(20)

#6.FINANCIAL APPLICATIONS
#OOP can be used to model financial entities like accounts, transactions, and reports.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Example usage
account = BankAccount("123456789")
account.deposit(500)
account.withdraw(200)

#7.CONTENT MANAGEMENT SYSTEM
#Classes can represent articles, authors, and comments in a CMS.

class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Author:
    def __init__(self, name):
        self.name = name
    
    def write_article(self, title, content):
        return Article(title, content)

# Example usage
author = Author("Alice")
article = author.write_article("My Article", "Content here...")











