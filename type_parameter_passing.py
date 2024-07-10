#type of parameter passing

# type-1 required argument

# def employee(eid, ename, email):
#     print(f"Eid: {eid}, Ename:{ename},Email:{email}")

# employee(10,"naina","naina@gmail.com")

#type-2  positional argument-->> Positional arguments are arguments that need to be included in the proper position or order

# def employee(eid, ename, email):
#     print(f"Eid: {eid}, Ename:{ename},Email:{email}")

# employee(10,"naina","naina@gmail.com")
# employee("naina",10,"naina@gmail.com")  #not order postion properly


#type--3  keyword argument --->>Keyword arguments (or named arguments) are values that, when passed into a function, are identifiable by specific parameter names. 


# def employee(eid, ename, email):
#     print(f"Eid: {eid}, Ename:{ename},Email:{email}")

# employee(ename="naina",eid=10, email="naina@gmail.com")


#type -4 keyword +positional argument--->


# def employee(eid, ename, email):
#     print(f"Eid: {eid}, Ename:{ename},Email:{email}")

# employee(10,ename="naina", email="naina@gmail.com")
# employee(10,"naina",email="naina@gmail.com")


#type -5 default argument-->>

# def employee(eid, ename, email):
#     print(f"Eid: {eid}, Ename:{ename},Email:{email}")

# employee(10,"naina","naina@gmail.com")


#----------------------variable length argument--------------------


# def employee(eid, ename, email):
#     print(f"Eid: {eid}, Ename:{ename},Email:{email}")

# employee(10,"naina")


# def employee ( *data):
#     print(data,type(data))

# employee()
# employee(10,20,30)
# employee(30,"hey")


def employee ( **data):
    print(data,type(data))

employee(eid= 10,ename="abhishek")

employee(email="abhuishek@gmail.com")

employee()

mytuple = (10,20)
print(mytuple[1])

