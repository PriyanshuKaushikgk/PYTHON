# 1 . User will input (3ages).Find the oldest one
# age1  = int(input("Enter age 1:"))
# age2  = int(input("Enter age 2:"))
# age3  = int(input("Enter age 3:"))
# if(age1>age2 and age1>age3):
#     print("age first is greater ")

# elif(age2>age1 and age2>age3):
#     print("Age second is greater")

# else:
#     print("Age third is greater")


# 2. Write a program that will convert celsius value to fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

if isinstance(celsius, (int, float)):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
else:
    print("Invalid input! Please enter a numeric value.")
