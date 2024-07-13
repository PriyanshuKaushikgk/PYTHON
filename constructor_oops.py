class employee:
    language = "python"
    salary = 1200000

    def __init__(self,name,salary,language):   #dundar method
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating a object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is{self.salary}")
        

    @staticmethod
    def greet():
        print("good night")


harry = employee("herry",1300000,"java")
# harry.name = "Harry"

print(harry.name,harry.salary,harry.language)


#-----------------------------------QUESTION-------------------------------------------

#Q.1 
class programer:
    company = "microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programer("jerry",1200000,321001)
print(p.name,p.salary,p.pin,p.company )

r = programer("tonny",1252400000,301001)
print(r.name,r.salary,r.pin,r.company )


#Q.2 write a class "calculator " capable of finding square,cube and square root of a number.


class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"the square is{self.n*self.n}")
    def cube_square(self):
        print(f"the cube_square is{self.n*self.n*self.n}")
    def square_root(self):
        print(f"the square_root is{self.n**1/2}")

a = calculator(4)
a.square()
a.cube_square()
a.square_root()
        


