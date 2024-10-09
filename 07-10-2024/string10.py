str = input('enter a string')
alapabet = 0 
digit = 0
special_char = 0
for i in str :
    if i.isalpha() :
        alphabet += 1
    elif i.isdigit() :
        digit += 1
    else:
        special_char += 1
    print('alabets are', alphabet)  
    print('digits are', digit)
    print('special characters are',special_char)