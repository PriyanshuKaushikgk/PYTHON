# Q.1
for i in range(1,5):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

# Q.2
for i in range(1,5):
    for j in range(1, i + 1):
        print(i, end=' ')
    print('')

#Q.3

col = 1
n = 1
for i in range(1,5):
    for j in range(1,col + 1):
        print(n,end=" ")
        n = n+1
    col = col+ 1
    print()


# Q.4
n  =  int(input("Enter the number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


# Q.3
start = 10
for i in range(1,5):
    for j in range(i):
        print(start, end=" ")
        start = start - 1
    print()

# Q.4
for i  in range(1,5):
    for j in range(65,65+i):
        a =  chr(j)
        print (a,end=" "),
    print()


# Q.5
start = 65
for i in range(0, 3):
    for j in range(0, i + 1):
         a = chr(start)
         print(f"{a}", end=" ")
         start += 1
    print("") 


#Q.6
def generate_pattern():
    num = 1
    letter = ord('a')
    for row in range(1, 5):
        for col in range(row):
            print(f"{num}{chr(letter)}", end=" ")
            num += 1
            letter += 1
        print()

generate_pattern()




#Q . 7
def generate_pattern(n):
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i or i == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

generate_pattern(5)



