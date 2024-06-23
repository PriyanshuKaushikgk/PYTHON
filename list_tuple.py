# mylist = [1.0,10,20,60.0,5,30]
# newlist = []

# for i in mylist:
#     if (type(i) is int):
#         newlist.append(i**2)

#         print(newlist)


# mylist = [1.0,10,20,60.0,5,30]
# for i in mylist:
#     if(type(i) is int):
#         print(i)


# mylist = ["hello","hey", "tushar", "Regex"]
# newlist=[]
# for i in mylist:
#     newlist.append(len(i))
# print(newlist)


# TUPLE
# IMMUTABLE
#MULTIPLE DATATYPEELEMENT
# INDEX POSITION
#FASTER

# mytuple = 10
# print(type(mytuple))

# mytuple = 10,20,"hey"
# print(type(mytuple))


#------------++++++++==================>>>>>>>>>>>>>>>>>>>>>

# mylist = []
# print(type(mylist))

# mylist = [10,20,30,"hello"]
# print(mylist)


# mylist = [10,20,30,"hello"]
# print(mylist[1:3])



#update
# mylist = [10,20,30,60.0,"hello"]
# mylist[0]=50
# print(mylist)


# mylist = [10,20,30,"hello"]
# mylist.append(70)
# print(mylist)

# mylist = [10,20,30,"hello"]
# mylist.extend([22,33,25,100])
# print(mylist)

# mylist = [10,20,30,"hello"]
# mylist.pop()
# print(mylist)


# mylist = [10,20,30,"hello"]
# mylist.pop(1)
# print(mylist)

# mylist = [10,20,30,"hello"]
# y = mylist.pop()
# print(mylist)
# print(y)

# mylist = [10,20,30,"hello"]
# mylist.insert(1,"om")
# print(mylist)


# mylist = [20,20,30,"hello",20,200,220,254,20,54]
# mylist.remove(20)
# print(mylist)


# mylist = [10,20,30,"hello",50]
# mylist[0:2]=[]
# print(mylist)


#index
# mylist = [10,20,30,"hello"]
# print(len(mylist))

# mylist = [10,20,30,"hello"]
# len(mylist)

# count = 0
# while(count<5):
#     print(mylist)
#     count+=1

# mylist = [10,20,30,60.02,"hello"]

# for i in mylist:
#     if(type(i) is int):
#         print(i)


# mylist = [10,20,30,60.02,"hello"]
# newlist=[]
# for i in mylist:
#     if(type(i) is int):
#         newlist.append(i**2)
#         # print(i)
#         print(newlist)



# mylist = ["hello", "hey", "tushar","regex"]
# newlist = []
# for i in mylist:
#     newlist.append(len(i))
# print(newlist)



#---------TUPLE-----------------===>>>>>>>>>>>>
# mytuple = 10,20
# print(type(mytuple))

# mytuple = 10,20,"hey"
# print(mytuple)
# print(mytuple[0])


# Accept input from the user
input_str = input("Enter a string: ")

# Initialize an empty result string
result_str = ""

# Iterate through each character in the input string
for char in input_str:
    # Check if the character is uppercase
    if 'A' <= char <= 'Z':
        # Convert to lowercase by adding the difference between 'a' and 'A'
        result_str += chr(ord(char) + (ord('a') - ord('A')))
    # Check if the character is lowercase
    elif 'a' <= char <= 'z':
        # Convert to uppercase by subtracting the difference between 'a' and 'A'
        result_str += chr(ord(char) - (ord('a') - ord('A')))
    else:
        # For non-alphabetic characters, keep them as they are
        result_str += char

# Print the result
print("Output: ", result_str)








