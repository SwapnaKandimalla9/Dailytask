# python program to check a string is palindrome or not
n = "peace"
rev=""
temp=n
for i in n:
    rev=i+rev
    if temp==rev:
        print("palindrome")
    else:
        print("not palindrome")