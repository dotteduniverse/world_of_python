#Functions: define 5 functions — square, greet, add, is_even, reverse_string
def square(a):
  return a*a
def greet(name):
  print(f"Hello! {name}")
def add(a,b):
    return a+b
def is_even(num):
    if num % 2 == 0:
         return True
    else:
         return False


def reverse_string(s):
   return s[::-1]

#test functions
print(square(10))
greet("Veera")
print(add(5, 3))
print(is_even("11"))
print(reverse_string("hello"))