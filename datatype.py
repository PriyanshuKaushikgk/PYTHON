x = 10
print(id(x))

y=x
print(id(y))

age= 18
print(id(age))

# id is use for memory address.
salary=age
print(id(salary))
salary=20
print("New",id(salary))

