#Exercises: Level 1
#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("sis1","sis2","sis3")
brothers = ("bro1","Bro2","Bro3","Bro4")

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters +brothers

#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings +("Father","Mother")

#Exercises: Level 2
#Unpack siblings and parents from family_members
siblings = family_members[0:7]
parents = family_members[7:]
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign 
# it to a variable called food_stuff_tp.
friuts = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage","Onion", "Carrot")
animal_products = ("milk","meat","egg")
food_stuff_tp = friuts + vegetables + animal_products

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[middle_index - 1: middle_index + 1]
else:
    middle_items = food_stuff_tp[middle_index]
print(middle_items)
#Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
print("banana" in friuts) # True

#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries) # False
#Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries) # True
