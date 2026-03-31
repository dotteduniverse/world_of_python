# List Comprehension
# List comprehension is a concise way to create lists in Python. 
# It allows you to generate a new list by applying an expression to each item in an iterable, 
# while optionally filtering items using a condition.
# Basic Syntax:
# new_list = [expression for item in iterable if condition]
# Example 1: Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#Filter only negative and zero in the list using list comprehension
#umbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)  # Output: [-4, -3, -2, -1, 0]

#Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#output   [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for sublist in list_of_lists for num in sublist]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9] 

'''
Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(result)
