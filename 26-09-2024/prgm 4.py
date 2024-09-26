# program to check if a string is palindrome.a palindrome is a word,pharse,or,sequence that reads the same forward and backword
def is-palindrome(s):
normalized-str=''.join(s.split()).lower()
return normalized-str==normalizes-str[::-1]
user-input=input("enter a word or pharse:")
if is_palindrome(user_input):
    print("user-input" is a palindrome.)
else:
    print("{user_input}" is not  a palindrome.')