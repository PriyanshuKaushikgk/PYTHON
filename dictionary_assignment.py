#Question.1 ======>>>
# s = "{[()]}"

# bracket_map = {')': '(', '}': '{', ']': '['}
# stack = []
# valid = True

# for char in s:
#     if char in bracket_map:
#         top_element = stack.pop() if stack else '#'
#         if bracket_map[char] != top_element:
#             valid = False
#             break
#     else:
#         stack.append(char)

# if stack:
#     valid = False

# print(valid)



#Question .2 ===>
data = "regex Software"
words = data.split()
capitalized_words = [word[:-1] + word[-1].upper() for word in words]
result = ' '.join(capitalized_words)
print(result)

