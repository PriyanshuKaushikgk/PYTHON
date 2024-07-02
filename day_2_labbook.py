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
# def find_longest_word_lambda(words):
  
#   return max(words,key=len)

# words=["apple","banana","heymynameispriyanshukaushik"]
# longest_word_length = find_longest_word_lambda(words)
# print(f"the length of the longest word is:{longest_word_length}")



#Q.5
# filter_long_words_lambda = lambda words, n: list(filter(lambda word: len(word) > n, words))

# words_list = ["apple", "banana", "cherry", "date"]
# n = 5
# print(filter_long_words_lambda(words_list, n))  

# #Q.6

# import string

# def is_palindrome(phrase):
#     normalized = ''.join(char.lower() for char in phrase if char.isalnum())
#     return normalized == normalized[::-1]

# phrases = [
#     "Go hang a salami I'm a lasagna hog.",
#     "Was it a rat I saw?",
#     "Step on no pets",
#     "Sit on a potato pan, Otis",
#     "Lisa Bonet ate no basil",
#     "Satan, oscillate my metallic sonatas",
#     "I roamed under it as a tired nude Maori",
#     "Rise to vote sir",
#     "Dammit, I'm mad!"
# ]

# for phrase in phrases:
#     print(f'"{phrase}" -> {is_palindrome(phrase)}')


# #Q.7

# import string

# def is_pangram(sentence):
#     alphabet_set = set(string.ascii_lowercase)
#     sentence_set = set(char.lower() for char in sentence if char.isalpha())
#     return alphabet_set <= sentence_set

# sentences = [
#     "The quick brown fox jumps over the lazy dog",
#     "Pack my box with five dozen liquor jugs",
#     "Sphinx of black quartz, judge my vow",
#     "This is not a pangram"
# ]

# for sentence in sentences:
#     print(f'"{sentence}" -> {is_pangram(sentence)}')


# #Q.8

# lexicon = {
#     "merry": "god",
#     "christmas": "jul",
#     "and": "och",
#     "happy": "gott",
#     "new": "nytt",
#     "year": "år"
# }

# def translate(english_words):
#     return [lexicon[word.lower()] for word in english_words if word.lower() in lexicon]

# english_sentence = ["Merry", "Christmas", "and", "Happy", "New", "Year"]
# swedish_translation = translate(english_sentence)

# print(swedish_translation)  

# #Q.9

# def char_freq(s):
#     freq_dict = {}
#     for char in s:
#         if char in freq_dict:
#             freq_dict[char] += 1
#         else:
#             freq_dict[char] = 1
#     return freq_dict

# string = "abbabcbdbabdbdbabababcbcbab"
# frequency = char_freq(string)

# print(frequency) 

# #Q.10
# # mathematics.py

# def add(*args):
#     return [sum(values) for values in zip(*args)]

# def sub(*args):
#     return [values[0] - sum(values[1:]) for values in zip(*args)]

# def sort_values(values):
#     return sorted(values)

# def max_value(*args):
#     return max(max(arg) for arg in args)

# def min_value(*args):
#     return min(min(arg) for arg in args)




# # main.py

# import mathematics

# a = [1, 2, 3, 4, 5]
# b = [5, 4, 3, 2, 1]

# c = mathematics.add(a, b)
# print(f"Sum of a and b: {c}")

# d = mathematics.sub(a, b)
# print(f"Difference of a and b: {d}")

# min_c = mathematics.min_value(c)
# min_d = mathematics.min_value(d)
# print(f"Minimum value in c: {min_c}")
# print(f"Minimum value in d: {min_d}")

# max_c = mathematics.max_value(c)
# max_d = mathematics.max_value(d)
# print(f"Maximum value in c: {max_c}")
# print(f"Maximum value in d: {max_d}")

# sorted_c = mathematics.sort_values(c)
# sorted_d = mathematics.sort_values(d)
# print(f"Sorted c: {sorted_c}")
# print(f"Sorted d: {sorted_d}")





