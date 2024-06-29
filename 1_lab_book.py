#Q.1
# name = "Priyanshu"
# print(f"Hello,{name}")

#Q.2
# num1 = float(input("Enter the first number:"))
# num2 = float(input("Enter the Second number:"))
# sum = num1 + num2
# print(sum)
# if(sum>0):
#     print("The sum is positive.")
# elif(sum<0):
#     print("The sum is negative.")
# else:
#     print("The sum is zero.")

#Q.3

# num = 5
# while True:
#     guess_number = int(input("Enter the number:"))
#     if guess_number == num:
#         print("correct!")
#         break
#     else:
#         print("Try again")


#Q.4
# firstname = input("Enter the first name:")
# lastname = input("Enter the last name:")

# wholename = firstname + " "  + lastname

# print(wholename)

#Q.6
# def sum_list(numbers):
#     return sum(numbers)

# def multiply_list(numbers):
#     result = 1
#     for number in numbers:
#         result *= number
#     return result


# numbers = [1, 2, 3, 4]
# print("Sum:", sum_list(numbers))    
# print("Multiplication:", multiply_list(numbers)) 

#Q.7
# def is_member(x, a):
#     for item in a:
#         if item == x:
#             return True
#     return False

# x = 10
# a = ["hey priyanshu" , 10 , 20]
# print(is_member(x, a))  

# x = 6
# a = [1, 2, 3, 4, 5]
# print(is_member(x, a)) 

#Q.8
# list1 = ['apple','banana','cherry']
# list2 = ['grapes','banana','kiwi']
# found_common = False

# for item1 in list1:
#     for item2 in list2:
#         if item1 == item2:
#             found_common = True
#             break
#     if found_common:
#         break
# print(found_common)


#Q.9
# numbers =  [4,9,7]
# for number in numbers:
#     print('*' * number  )


#Q. 10
# hundred_meters = ['Vikay', 'John', 'Kumar', 'Rajesh', 'Malar', 'Vaihai']
# two_hundred_meters = ['Vetry', 'Petter', 'Priyanka', 'Kumar', 'Malar']

# set_hundred_meters = set(hundred_meters)
# set_two_hundred_meters = set(two_hundred_meters)

# only_hundred_meters = set_hundred_meters - set_two_hundred_meters
# print("Athletes who participated only in 100m race:", list(only_hundred_meters))

# only_two_hundred_meters = set_two_hundred_meters - set_hundred_meters
# print("Athletes who participated only in 200m race:", list(only_two_hundred_meters))

# both_races = set_hundred_meters & set_two_hundred_meters
# print("Athletes who participated in both 100m and 200m race:", list(both_races))

# only_one_race = (set_hundred_meters ^ set_two_hundred_meters)
# print("Athletes who participated in only one race:", list(only_one_race))





#Q.11
# numbers = [5, 8, 4, 18, 8, 55, 6, 8, 3, 18, 5, 3, 44]

# counts = {}

# duplicates = []

# for number in numbers:
#     if number in counts:
#         counts[number] += 1
#     else:
#         counts[number] = 1

# for number in counts:
#     if counts[number] > 1:
#         duplicates.append(number)

# print("Duplicate numbers:", duplicates)

#Q.12
# list_of_animals = ["cat", "tiger", "lion", "zebra", "crocodile", "snack"]

# reversed_list = []

# for i in range(len(list_of_animals) - 1,-1,-1):
#     reversed_list.append(list_of_animals[i])

# print(reversed_list)




#---------------PATTERN------------------------------------------

#.1
    #  A
  #   A B
  #  A B C


# for i in range(3):
#     for j in range(3 - i - 1):
#         print(" ", end="")

#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")

#     print()


#Q.2
  
# * * * * * 
 #  * * * 
  #   *

# for i in range (3):
#     for j in range(i):
#         print(" ",end="")
    
#     for j in range(2 * (3-i)-1):
#         print("* ",end="")
    
#     print(" ")


#Q. 3

# for i in range(3):
#     for j in range(3-i-1):
#         print(" ", end="")
    
#     for j in range(i+1):
#         print(10+i,end=" ")
#     print()


#Q.4

# for i in range(3):
#     for j in range(3-i-1):
#         print(" ",end="")

#     for j in range(2 * i+1):
#         print(chr(ord('A')+j),end="")
#     print()




#Q.5

# for i in range(5):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(5-i):
#         print("* ",end="")
#     print()


# what is namespace
#A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves.


# Difference between == and is operator
#The == operator is used to compare the equality of objects. The is operator is used to check if different variables are pointing to the same object in memory.

# diffenrence between list and tuple.

# LIST
#      Lists are mutable
#      The implication of iterations is Time-consuming
#      list is better for performing operations, such as insertion and deletion.
#      Lists consume more memory
#      Lists have several built-in methods
# TUPLE:---

# 1	Tuples are immutable
# 2	The implication of iterations is comparatively Faster
# 3 	A Tuple data type is appropriate for accessing the elements
# 4	Tuple consumes less memory as compared to the list
# 5	Tuple does not have many built-in methods.