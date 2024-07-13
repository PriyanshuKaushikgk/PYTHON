# x = 10
# print(id(x))

# y=x
# print(id(y))

# age= 18
# print(id(age))

# # id is use for memory address.
# salary=age
# print(id(salary))
# salary=20
# print("New",id(salary))

# def reverse_and_swap_case(s):
#     word=s.split(' ')
#     reversed_words = words[::-1]
#     result = ' '.join(word.swapcase() for word in reversed_words)
#     return result
    
    
# input_string = "aWESOME is cODING"
# output_string = reverse_and_swap_case(input_string)
# print(output_string)


# def missingCharacters(s):
#     digits = set('0123456789')
#     letters =set('abcdefghijklmnopqrstuvwxyz')
    
    
#     input_set = set(s)
    
    
#     missing_digits = sorted(digits-input_set)
#     missing_letters = sorted(letters-input_set)
    
#     return '',join(missing_digits) + ''.join(missing_letters)
    
# input_string = "7985interdisciplinary12"
# output_string = missingCharacters(input_string)
# print(output_string)

a = input("Enter the string:")
b = input("enter another string:")
print(a)
print(b)