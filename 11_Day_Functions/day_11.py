
#1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(3,4))
#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def area_of_circle(r):
    pi = 3.14
    return pi * r * r
print(area_of_circle(5))
#3. Write a function called add_all_nums which takes arbitrary number of arguments 
# and sums all the arguments. Check if all the list items are number types. 
# If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "All items must be numbers."
    return total
print(add_all_nums(1, 2, 3, 4))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
#  Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(convert_celsius_to_fahrenheit(25))

#5. Write a function called check-season, it takes a month parameter and 
# returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Invalid month"
print(check_season("March"))

#6. Write a function called calculate_slope which return the slope of a linear equation y = mx + c. The function takes m as a parameter and returns the slope.
import math
def calculate_slope(m,x,c):
    y= m*x + c
    return m    
print(calculate_slope(2,3,4))

#7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"
print(solve_quadratic_eqn(1, -3, 2))
#8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)
print_list([1, 2, 3, 4, 5])

#9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
print(reverse_list([1, 2, 3, 4, 5]))

#10. Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns the capitalized list of items.
def capitalize_list_items(lst):
    capitalized_lst = []
    for item in lst:
        capitalized_lst.append(item.capitalize())
    return capitalized_lst
print(capitalize_list_items(['apple', 'banana', 'cherry']))
#11. Declare a function named add_item. It takes a list and an item parameters, 
# it returns a list with the item added at the end.
'''
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
'''
def add_item(lst, item):
    lst.append(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]  
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
#12. Declare a function named remove_item. It takes a list and an item parameters,
#  it returns a list with the item removed from it.
'''
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
'''
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

#13. Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
'''
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
'''
def sum_of_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

#14. Declare a function named sum_of_odds. It takes a number parameter and 
# it adds all the odd numbers in that range.

def sum_of_odds(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total
print(sum_of_odds(5))  # 9
print(sum_of_odds(10)) # 25
print(sum_of_odds(100)) # 2500

#15. Declare a function named sum_of_evens. It takes a number parameter and 
# it adds all the even numbers in that range.
def sum_of_evens(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_evens(5))  # 6
print(sum_of_evens(10)) # 30    
print(sum_of_evens(100)) # 2550
'''Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
    '''
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."
print(evens_and_odds(100))
#Call your function factorial, it takes a whole number as a parameter 
# and it return a factorial of the number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
print(factorial(5))  # 120
print(factorial(0))  # 1  
print(factorial(-3)) # Factorial is not defined for negative numbers.

#Declare a function named is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if not param:
        return "The parameter is empty."
    else:
        return "The parameter is not empty."
print(is_empty(""))  # The parameter is empty.
print(is_empty("Hello"))  # The parameter is not empty.
#Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)
def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        median = sorted_lst[n//2]
    return median
def calculate_mode(lst):
    from collections import Counter
    data = Counter(lst)
    mode_data = data.most_common()
    mode = [num for num, count in mode_data if count == mode_data[0][1]]
    return mode
def calculate_range(lst):
    return max(lst) - min(lst)
def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
def calculate_std(lst):
    variance = calculate_variance(lst)
    return variance ** 0.5
numbers = [1, 2, 3, 4, 5, 5]
print("Mean:", calculate_mean(numbers))  # Mean: 3.3333333333333335
print("Median:", calculate_median(numbers))  # Median: 3.5      
print("Mode:", calculate_mode(numbers))  # Mode: [5]
print("Range:", calculate_range(numbers))  # Range: 4
print("Variance:", calculate_variance(numbers))  # Variance: 1.5555555555555555
print("Standard Deviation:", calculate_std(numbers))  # Standard Deviation: 1.247219128924647

'''Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
   '''
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # "Hello, Guest!"
greet("Alice")  # "Hello, Alice!"
'''
Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
'''
def show_args(**kwargs):
    args_str = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    print(f"Received: {args_str}")
show_args(name="Alice", age=30, city="New York")  # Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")  # Received: name: Bob, pet: Fluffy, the bunny

#Exercises: Level 3
#Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))  # True
print(is_prime(10)) # False
print(is_prime(13)) # True  

#Write a functions which checks if all items are unique in the list.
def are_all_items_unique(lst):
    return len(lst) == len(set(lst))
print(are_all_items_unique([1, 2, 3, 4]))  # True
print(are_all_items_unique([1, 2, 3, 4, 2]))  # False

#Write a function which checks if all the items of the list are of the same data type.
def are_all_items_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)
print(are_all_items_same_type([1, 2, 3, 4]))  # True
print(are_all_items_same_type([1, "2", 3, 4]))  # False

#Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True
print(is_valid_variable("my_variable"))  # True
print(is_valid_variable("2variable"))  # False
print(is_valid_variable("for"))  # False

#Go to the data folder and access the countries-data.py file.
from countries_data import data


#Create a function called the most_spoken_languages in the world.
#  It should return 10 or 20 most spoken languages in the world in descending order

def most_spoken_languages(n=10):
    language_count = {}
    for country in data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]
print(most_spoken_languages(10))

#Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.

def most_populated_countries(n=10):
    population_count = [(country['name'], country['population']) for country in data]
    sorted_population = sorted(population_count, key=lambda x: x[1], reverse=True)
    return sorted_population[:n]
print(most_populated_countries(10))
