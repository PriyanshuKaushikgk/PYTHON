# loop
#for loop
# range : 0, 10 , 1 (start, stop ,[step=1] )
# in c language for loop is => for ( i= 0;i<10;i++)
# in python for loop => 
# for i in range(0,11):
#     print(i)


# for i in range(0,11,2):
#     print(i)


# for i in range(4,14,3):
#     print(i)

# for x in range(10,0,-1):
#     print(x)

#Question => to print all the even number from 1 to 7.
# for i in range(1,7):
#     if(i%2==0):
#         print(i)

#Question => starting k 5 natural number ka sum calculate krna hai.
# total = 0
# for i in range (1,7):
#     total = total+i
# print(total)


#Question=> run a loop 100 to 2 and we need to calculate the sum of which divisible by 7.

# total = 0
# for i in range(100,1,-1):
#     if (i%7==0):
#         total +=i
# print(total)


#string
# for x in "hello":
#     print(x)


# data = "regex"
# for char in data :
#     print(char,end="")

#Question => run a for loop over a string data and find out how many characters in string.
# c=0
# for x in "hello":
#     c= c+1
# print(c)


# data ="Priyanshukaushik"
# total = 0
# for char in data:
#     total+=1
# print(total)

# string data using index
# print(len("priyanshu"))


# data = "priyanshu"

# for i in range(0,9):
#     print(i,"=",data[i])


# data = "jaipur012345"
# for i in range(0,len(data)):
#     print(i,"=",data[i])


#Question=> run a for loop over a string data and print all the vowels in string.
# vowels = "aeiou"
# data= "hey ram how are you shyam says that i am okkey"
# for char in data:
#     if(char in vowels):
#       print(char)



# for x in "jaipur":
#    if(x in "aeiou"):
#       print("Vowel is :", x)


for x in "priyanshu":
   if(x=="a" or x =="e" or x=="i" or x=="o" or x=="u"):
      print("Vowel is :", x)






