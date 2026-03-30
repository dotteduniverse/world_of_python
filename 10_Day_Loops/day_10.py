#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total = 0
for i in range(101):
    total += i
print(f"The sum of all numbers from 0 to 100 is: {total}")
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")
print(f"The sum of all evens from 0 to 100 is: {even_sum}")
print(f"The sum of all odds from 0 to 100 is: {odd_sum}")

#1. Go to the data folder and use the [countries.py] file. 
# Loop through the countries and extract all the countries containing the word _land_.
from countries_data import countries
countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country) 
print("Countries containing the word 'land':")
for country in countries_with_land: 
    print(country)

#1. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruit list:")
print(reversed_fruits)

#1. Go to the data folder and use the [countries_data.py] file.
#   1. What are the total number of languages in the data
#   2. Find the ten most spoken languages from the data
#   3. Find the 10 most populated countries in the world

from countries import data
# Total number of languages
languages = set()
for country in data:
    for language in country['languages']:
        languages.add(language)
print(f"Total number of languages: {len(languages)}")
# Ten most spoken languages
language_count = {}
for country in data:
    for language in country['languages']:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1
sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
print("Ten most spoken languages:")
for language, count in sorted_languages[:10]:
    print(f"{language}: {count}")
# Ten most populated countries
sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)    
print("Ten most populated countries:")
for country in sorted_countries[:10]:
    print(f"{country['name']}: {country['population']}")

    
