#1. Explain the difference between map, filter, and reduce.
# Map, filter, and reduce are higher-order functions in Python that operate on iterables.
# - Map: The map function applies a given function to each item of an iterable and returns a map object (which is an iterator). It is used to transform each item in the iterable.
# Example:
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
# - Filter: The filter function constructs an iterator from elements of an iterable for which a function returns true. It is used to filter items in the iterable based on a condition.
# Example:
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]
# - Reduce: The reduce function is used to apply a rolling computation to sequential pairs of values
# in an iterable. It is part of the functools module and is used to reduce a list to a single value by applying a binary function cumulatively to the items.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120


#2. Explain the difference between higher order function, closure and decorator
# - Higher-order function: A higher-order function is a function that takes one or more functions
#  as arguments and/or returns a function as its result. Examples include map, filter, and reduce.
# - Closure: A closure is a function that has access to variables from its outer (enclosing) 
# scope even after the outer function has finished executing.
# - Decorator: A decorator is a design pattern in Python that allows modifying the behavior of a function or class
#  without permanently altering it. It is a function that takes another function as an argument and returns a function as its result.


#3. Define a call function before map, filter or reduce, see examples.
def call(func, *args, **kwargs):
    return func(*args, **kwargs)
# Example usage:
def add(x, y):
    return x + y
result = call(add, 5, 3)
print(result)  # Output: 8

#4. Use for loop to print each country in the countries list.
from countries import countries
for country in countries:
    print(country)

#5. Use for to print each name in the names list.
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
for name in names:
    print(name)

#6. Use for to print each number in the numbers list.
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#1. Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = map(lambda x: x.upper(), countries)
print(list(upper_countries))

#1. Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

#1. Use map to change each name to uppercase in the names list
upper_names = map(lambda x: x.upper(), names)
print(list(upper_names))
#1. Use filter to filter out countries containing 'land'.
countries_with_land = filter(lambda x: 'land' in x, countries)
print(list(countries_with_land))

#1. Use filter to filter out countries having exactly six characters.
countries_with_six_characters = filter(lambda x: len(x) == 6, countries)
print(list(countries_with_six_characters))
#1. Use filter to filter out countries containing six letters and more in the country list.
countries_with_six_or_more_characters = filter(lambda x: len(x) >= 6, countries)
print(list(countries_with_six_or_more_characters))

#1. Use filter to filter out countries starting with an 'E'
countries_starting_with_e = filter(lambda x: x.startswith('E'), countries)
print(list(countries_starting_with_e))


#1. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# Example: numbers.map(lambda x: x**2).filter(lambda x: x > 10).reduce(lambda acc, x: acc + x, 0)
squared_numbers = map(lambda x: x**2, numbers)
filtered_numbers = filter(lambda x: x > 10, squared_numbers)
result = reduce(lambda acc, x: acc + x, filtered_numbers, 0)
print(result)  # Output: 29 (16 + 25)

#1. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
# Example usage:
mixed_list = [1, 'hello', 3.14, 'world', True, 'python']
string_list = get_string_lists(mixed_list)
print(string_list)  # Output: ['hello', 'world', 'python']

#1. Use reduce to sum all the numbers in the numbers list.
total_sum = reduce(lambda acc, x: acc + x, numbers, 0)
print(total_sum)  # Output: 15

#1. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
north_european_countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(lambda acc, x: acc + ', ' + x if acc else x, north_european_countries) + ' are north European countries'
print(sentence)  # Output: Estonia, Finland, Sweden, Denmark, Norway, and Iceland

#1. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(pattern):
    return list(filter(lambda x: pattern in x, countries))  
# Example usage:
countries_with_land = categorize_countries('land')
print(countries_with_land)  # Output: ['Finland', 'Iceland', 'Ireland', 'Netherlands', 'Poland', 'Switzerland', 'Thailand']

#1. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_starting_letter():
    country_count = {}
    for country in countries:
        starting_letter = country[0].upper()
        if starting_letter in country_count:
            country_count[starting_letter] += 1
        else:
            country_count[starting_letter] = 1
    return country_count
country_count = count_countries_by_starting_letter()
print(country_count)

#2. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries():
    return countries[:10]

#1. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries():
    return countries[-10:]

'''
1. Use the countries_data.py  file and follow the tasks below:
   - Sort countries by name, by capital, by population
   - Sort out the ten most spoken languages by location.
   - Sort out the ten most populated countries.
'''
from countries_data import data
# Sort countries by name
sorted_by_name = sorted(data, key=lambda x: x['name'])
print("Countries sorted by name:")
for country in sorted_by_name:
    print(country['name'])
# Sort countries by capital
sorted_by_capital = sorted(data, key=lambda x: x['capital'])
print("\nCountries sorted by capital:")
for country in sorted_by_capital:
    print(country['capital'])
# Sort countries by population
sorted_by_population = sorted(data, key=lambda x: x['population'], reverse=True)    
print("\nCountries sorted by population:")
for country in sorted_by_population:
    print(f"{country['name']}: {country['population']}")
# Sort out the ten most spoken languages by location
from collections import Counter
languages = [language for country in data for language in country['languages']]
most_spoken_languages = Counter(languages).most_common(10)
print("\nTen most spoken languages by location:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")
# Sort out the ten most populated countries
most_populated_countries = sorted(data, key=lambda x: x['population'], reverse=True)[:10]
print("\nTen most populated countries:")
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")

    
