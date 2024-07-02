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


# def values(a,b):
#     if(a%6==0 and b%6==0):
#         print("hey")
#     else:
#         print("hello")
# a = int(input("Enter the values of a:"))
# b = int(input("Enter the values of b is :"))
# values(a,b)




#27/06/2024--------------------->>>>>>>>>>>>>>>>>

# #keyword+ opositional argument:
# def employee(eid,ename,email):
#     print(f"Eid:{eid},Ename:{ename},Email:{email}")

# employee("naina",ename=10,email="naina@gmail.com")


#default argument=> function declaration
# def employee(eid,ename,email):
#     print(f"Eid:{eid},Ename:{ename},Email:{email}")

# employee(10,"naina","naina@gmail.com")


#variable length argument
# def employee(*data):
#     print(data,type(data))

# employee()
# employee(10,20,30)
# employee(30,"hey")




# def func(x):
#     x=x+10
#     print("X is value in function:",x)
# num=10
# func(num)


#mutable data type

# def func(mylist):
#     print(mylist,type(mylist))
    # mylist.append(60)
    # print("inside function after change:",mylist,)

#outside
# list1=[10,20,30]
# print("Original:",list1,id(list1))
# func(list1)
# print("function call original :",list1,id(list1))



# Lambda function as call as annymous function
# one line-inline

# def square(x):
#     print(x**2)

# square(10)


#Lambda parameter: expression
# lambda x: x**2

# Lambda parameter: expression

# out = lambda  x: x**2
# out(10)



# def func(s):
#     total =0
#     for i in s :
#         total+=1
    
#     return{s:total}

# out = func("hey hello")
# print(out)


#high order funcitons
#all high order function are first class function

# def square(x):
#     return(x**2)

# def addValues(x,y):
#     print(x,y)

# addValues(10,square(20))
# print(addValues)


# def square(x):
#     return(x**2)

# def addValues(x,y):
#     print(x,y(30))

# addValues(10, square)


#lambda  =>> use argument

mylist = [10,20,30,40,50]

print(list(map(lambda x:x**2, mylist)))


#normal funciton
#args and kwargs
#lambda funtion
#normal and lambda fjucntion
#first calss vs high order
#map and filter



