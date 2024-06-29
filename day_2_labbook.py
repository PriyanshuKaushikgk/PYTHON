# #Q.1

# def generate_n_chars(n, c):
#     return c * n

# print(generate_n_chars(5, "x"))  
# print(generate_n_chars(3, "$")) 

# #Q.2
# def max_in_list(numbers):
  

#   largest = numbers[0]

#   for number in numbers:
#     if number > largest:
#       largest = number

#   return largest

# numbers = [5, 10, 1, 9, 2]
# largest_number = max_in_list(numbers)
# print(f"The largest number in the list is: {largest_number}") 


# #Q.3
# def word_lengths_map(words):
  
#   return list(map(len, words))

# words = ["apple", "banana", "cherry"]
# word_lengths = word_lengths_map(words)
# print(word_lengths)  

#Q.4
def find_longest_word_lambda(words):
  
  return max(words,key=len)

words=["apple","banana","heymynameispriyanshukaushik"]
longest_word_length = find_longest_word_lambda(words)
print(f"the length of the longest word is:{longest_word_length}")


def find_longest_word_lambda(words):
  """Finds the length of the longest word in a list using a lambda expression.

  Args:
      words: A list of strings.

  Returns:
      The length of the longest word.
  """

  return max(words, key=len)

# Example usage (same as above)
words = ["apple", "banana", "cherry", "supercalifragilisticexpialidocious"]
longest_word_length = find_longest_word_lambda(words)
print(f"The length of the longest word is: {longest_word_length}")  # Output: The length of the longest word is: 34
