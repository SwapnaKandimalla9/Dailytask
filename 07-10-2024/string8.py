string1 = "see"
string2 = "you"
output = " ".join([string1,string2])
print(output)

string = "swapna"
new = ""
for i in string:
    if i not in new:
        new = new+i
        print(new)