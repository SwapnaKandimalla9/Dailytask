1 . E_commerce platform
#In an e-commerce application, classes can be used to model products, users, and orders.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def total_price(self):
        return self.product.price * self.quantity

# Example usage
product = Product("Laptop", 1200)
order = Order(product, 2)
print(order.total_price())  # Output: 2400

2. SOCIAL MEDIA APPLICATIONS

Classes can represent users, posts, and comments, encapsulating relevant behaviors.

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
    
    def create_post(self, content):
        post = Post(content, self.username)
        self.posts.append(post)

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.likes = 0
    
    def like(self):
        self.likes += 1

# Example usage
user = User("john_doe")
user.create_post("Hello, world!")
print(user.posts[0].content)  # Output: Hello, world!

3. BANKING SYSTEM 

#Classes can be used to model bank accounts, transactions, and users.

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
account.deposit(1000)
account.withdraw(500)
print(account.balance)  # Output: 500



