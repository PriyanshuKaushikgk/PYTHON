# # question 1
# a = 5
# b = 10

# print("Before swapping:")
# print("a =", a)
# print("b =", b)

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)

# # question 2
# num = 7536
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print("Reversed Number: " + str(reversed_num))


# # question 3
Number = int(input("Please Enter any Number: "))
Sum = 0

while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10

print("\n Sum of the digits of Given Number = %d" %Sum)

# question 4 
num = int(input("Enter a Number: "))
result = 0
hold = num

while num > 0:
    rem = num % 10
    result = result + rem
    num = int(num/10)

print("Sum of all digits of", hold, "is: ", result)

# Question 5 
Number = int(input("Please Enter the Number to Check: "))

Sum = 0
Times = 0

Temp = Number
while Temp > 0:
    Times = Times + 1
    Temp = Temp // 10

Temp = Number
while Temp > 0:
    Reminder = Temp % 10
    Sum = Sum + (Reminder ** Times)
    Temp //= 10

if Number == Sum:
    print("%d is Armstrong." %Number)
else:
    print("%d is Not." %Number)

