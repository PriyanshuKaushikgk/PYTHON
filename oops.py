# class house:
#     color = "white"
#     rooms = 4

#     def info(self):
#         print("house has",self.color,self.rooms)
# h1 = house()
# regex = house()
# regex.info()


# class house:
#     def __init__(self):
#         print("constructor bulaya")

# h1 = house()
# print("H1",h1)

# regex = house()
# print("regex",regex)


# class house:
#     def __init__(self,x):
#         print("constructor bulaya")

# h1 = house("yellow")
# h2 = house("red")



# class house:
#     def __init__(self,x):
#         self.color=x
# h1 = house("yellow")
# h1.color
        



# def sumNo(x,y):
#     c=x+y
#     print(c)
# sumNo(10,20)

# def f():
	
# 	# local variable
# 	s = "I love Geeksforgeeks"
# 	print("Inside Function:", s)

# # Driver code
# f()
# print(s)

# def add():
#       print("Inside function:",x+10)

# x = 10
# add()
# print(x)


#_--------------------------


class employee:
  def __init__(self,x,y,z):

    self.id=x
    self.name = y
    self.email = z
    print("Inside class = ",x,y,z)

h1 = employee(1,"yash","regex@gmail.com")
print("name=",h1.name)
print("eid=",h1.id)
print("Email=",h1.email)
print()
print(h1.id,h1.name,h1.email)
