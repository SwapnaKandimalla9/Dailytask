def is_digit(character): 
    return character.isdigit()
character = input("enter a character:")
if is_digit(character):
    print("character is a digit.")
else:
    print("character is not a digit.")
	