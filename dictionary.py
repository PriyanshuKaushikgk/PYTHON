mydictionary = {}
data  = "xyzxxxy"
for char in  data:
    if(char not in "aeiou"):
        if(char not in mydictionary):
            mydictionary[char]= 1
        else:
            mydictionary[char]= mydictionary[char]+1
print(mydictionary)