'''

1. Create  an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
4. Get the length of the student dictionary
5. Get the value of skills and check the data type, it should be a list
6. Modify the skills values by adding one or two skills
7. Get the dictionary keys as a list
8. Get the dictionary values as a list
9. Change the dictionary to a list of tuples using _items()_ method
10. Delete one of the items in the dictionary
11. Delete one of the dictionaries
'''
# 1. Create  an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'New York',
    'address': '123 Main Street'
}
# 4. Get the length of the student dictionary
student_length = len(student)
# 5. Get the value of skills and check the data type, it should be a list
skills = student['skills']
skills_type = type(skills)
# 6. Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
# 7. Get the dictionary keys as a list
student_keys = list(student.keys())
# 8. Get the dictionary values as a list
student_values = list(student.values())
# 9. Change the dictionary to a list of tuples using _items()_ method
student_items = list(student.items())
# 10. Delete one of the items in the dictionary
del student['marital_status']
# 11. Delete one of the dictionaries
del dog
