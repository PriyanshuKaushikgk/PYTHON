#function
#named block
#
# block of code that we can run any Time
#loop
#name
#code redability
#bade logic ==> logic mai convert 
# debugging is easier

#username => Parameter / formal/ informal /  
# def greeting():
#     name= "tushar"
#     print("hello",name)
# greeting()


# def sumNo(x,y):
#     c = x+y
#     print(c)


# x = 10
# y = 20
# sumNo()


# def func():
#     print("Inside function",x+10)
# x = 10
# func()
# print(x)


# def func():
#     global x
#     x = x+10
#     print("Inside function",x)
# x = 10
# func()
# print(x)

# def ageAdd():
#     global age
#     age = age +1
#     print("Inside function :",age)

# age=18
# ageAdd()
# print("Outside function:",age)



# def additionNo(num):
#     print("NUM",id(num))
#     print(num+10)
#     print("new num:",id(num))
# x = 10
# print("before function:",id(x))
# additionNo(x  )
# print("after function:",id(x))




# def divisible(val1, val2):
#     if val1 % 6 == 0 and val2 % 6 == 0:
#         print("Hey")
#     else:
#         print("Hello")

# divisible(12, 18)  
# divisible(12, 20)  
# divisible(7, 18)   
# divisible(6, 6)    

# ****
# ***
# **
# *

# def calculateGmean(a,b):
#     mean  = (a*b)/(a+b)
#     print(mean)
# calculateGmean(9,8)


# def isgreater (a,b):
#     if(a>b):
#         print("First number is greater then second number:",a)
#     else:
#         print("Second is greater the first :",b)

# isgreater(5,4)


# def average (a,b):
#     print("The average is:",(a+b)/2)

# average(5,4)

# --------AVERAGE OF MANY NUMBER PROGRAMM------------>>>>>>>>>>>>
# def average(*numbers):
#     print(type(numbers))
#     sum =0
#     for i in numbers:
#         sum = sum+i
#     print("average is :",sum/len(numbers))

# average(5,4,1)


# def evenOdd(n):
#     if (n%2==0):
#         print("True")
#     else:
#         print("False")
# n = int(input("Enter the number:"))

# evenOdd(n)


def values(a,b):
    if(a%6==0 and b%6==0):
        print("hey")
    else:
        print("hello")
a = int(input("Enter the values of a:"))
b = int(input("Enter the values of b is :"))
values(a,b)
