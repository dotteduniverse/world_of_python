#Exercises: Level 1
#Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))  # 7
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter'}

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Netflix', 'Airbnb'])
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'LinkedIn', 'Netflix', 'Airbnb'}

#Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon', 'Twitter', 'LinkedIn', 'Netflix', 'Airbnb'}

#What is the difference between remove and discard  
#The remove() method removes a specified element from the set. If the element is not found, it raises a KeyError.
#The discard() method also removes a specified element from the set, but if the element is not found, it does not raise an error and simply does nothing.

#Exercises: Level 2
#Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_union_B = A.union(B)
print(A)  # {19, 20, 22, 24, 25, 26}
print(B)  # {19, 20, 22, 24, 25, 26, 27, 28}
print(A_union_B)  # {19, 20, 22, 24, 25, 26, 27, 28}

#Find A intersection B
A_intersection_B = A.intersection(B)
print(A_intersection_B)  # {19, 20, 22, 24, 25, 26}

#Is A subset of B
is_A_subset_B = A.issubset(B)
print(is_A_subset_B)  # True

#Are A and B disjoint sets
are_A_and_B_disjoint = A.isdisjoint(B)
print(are_A_and_B_disjoint)  # False

#Join A with B and B with A
A_union_B = A.union(B)
B_union_A = B.union(A)
print(A_union_B)  # {19, 20, 22, 24, 25, 26, 27, 28}
print(B_union_A)  # {19, 20, 22, 24, 25, 26, 27, 28}

#What is the symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)
print(A_symmetric_difference_B)  # {27, 28}

#Delete the sets completely
del A
del B
#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)
print(len(ages))  # 8
print(len(ages_set))  # 5
#Explain the difference between the following data types: string, list, tuple and set
#String: A string is a sequence of characters enclosed in quotes. It is immutable, meaning it cannot be changed after it is created. Example: "Hello, World!"
#List: A list is an ordered collection of items that can be of different types. It is mutable, meaning it can be changed after it is created. Example: [1, 2, 3, 'four', 'five']
#Tuple: A tuple is an ordered collection of items that can be of different types. It is immutable, meaning it cannot be changed after it is created. Example: (1, 2, 3, 'four', 'five')
#Set: A set is an unordered collection of unique items. It is mutable, meaning it can be changed after it is created. Example: {1, 2, 3, 'four', 'five'}
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(unique_words)  # {'I', 'am', 'a', 'teacher', 'and', 'love', 'to', 'inspire', 'teach', 'people.'}
print(len(unique_words))  # 10

