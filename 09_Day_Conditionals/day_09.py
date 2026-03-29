'''
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_to_wait = 18 - age
    print(f"You need {years_to_wait} more years to learn to drive.")

'''
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
'''
age = int(input("Enter your age: "))
my_age = 25
if age > my_age:
    age_difference = age - my_age
    if age_difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_difference} years older than me.")
elif age < my_age:
    age_difference = my_age - age
    if age_difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_difference} years older than you.")
else:
    print("We are the same age.")

'''
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
'''
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))  
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

'''
Write a code which gives grade to students according to theirs scores:

90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
'''
score = float(input("Enter your score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid score'
print(f"Your grade is: {grade}")

'''
Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
If the user input is: September, October or November, the season is Autumn. December, January or February,
 the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
'''
month = input("Enter the month: ").strip().capitalize()
if month in ['September', 'October', 'November']:
    season = 'Autumn'
elif month in ['December', 'January', 'February']:
    season = 'Winter'
elif month in ['March', 'April', 'May']:
    season = 'Spring'
elif month in ['June', 'July', 'August']:
    season = 'Summer'
else:
    season = 'Invalid month'
print(f"The season is: {season}")

'''
The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')

'''
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Modified list of fruits:", fruits)


'''
Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Veera',
    'last_name': 'Malla Reddy',
    'age': 250,
    'country': 'India',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, 
    if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, 
    if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'),
   if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
   if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
   else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in India, 
 print the information in the following format:

'''
person={
    'first_name': 'Veera',
    'last_name': 'Malla Reddy',
    'age': 250,
    'country': 'India',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person.get('skills'):
    middle_skill_index = len(person['skills']) // 2
    middle_skill = person['skills'][middle_skill_index]
    print("Middle skill:", middle_skill)
if person.get('skills'):
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)
skills = person.get('skills', [])
if set(['JavaScript', 'React']).issubset(skills):
    print('He is a front end developer')
elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
    print('He is a backend developer')
elif set(['React', 'Node', 'MongoDB']).issubset(skills):
    print('He is a fullstack developer')
else:
    print('Unknown title')
if person.get('is_married') and person.get('country') == 'India':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")


