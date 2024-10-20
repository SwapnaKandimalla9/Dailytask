# program to create a dict from a string
input_string = "skywavessoftwares"
letter_count = {}
for char in input_string:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print (letter_count)

