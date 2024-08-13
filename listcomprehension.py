# When we process a list and we get a new list
celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fahrenheitvalues = []

# methods are nothing but functions inside and object
# to call a method, first you must have the object
# here fahrenheitvalues is the list object
# to call the method inside the list object we will use the dot (.) operator
# which is followed by the function name
# fahrenheitvalues.append(10)

for celciusvalue in celciusvalues:
    fahrenheitvalues.append((celciusvalue * 9 / 5) + 32)

print(celciusvalues)
print(fahrenheitvalues)

# we have pricelist lets us calculate the prices with sst
prices = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sstprices = []
for price in prices:
    sstprices.append(price + (price * 0.06))
    # print(sstprices)
print(prices)
print(sstprices)

fruits = ["apple", "orange", "mango"]
newfruits = fruits # this is not creating a copy rather referring to the same location
print(fruits)
print(newfruits)

fruits = ["apple", "orange", "mango"]
newfruits = []
for fruit in fruits:
    newfruits.append(fruit)
newfruits.append("rambutan")
print(fruits)
print(newfruits)

fruits = ["apple", "orange", "mango"]
newfruits = [fruit for fruit in fruits] # list comprehension
newfruits.append("grapes")
print(fruits)
print(newfruits)

celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
fahrenheitvalues = [((celciusvalue * 9/5) + 32) for celciusvalue in celciusvalues]
print(celciusvalues)
print(fahrenheitvalues)

prices = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sstprices = [(price + (price * 0.06)) for price in prices]
print(prices)
print(sstprices)

mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the even numbers only
evennumbers = []
oddnumbers = []
for mynumber in mynumbers:
    if (mynumber % 2 == 0):
        evennumbers.append(mynumber)
    else:
         oddnumbers.append(mynumber)
print(mynumbers)
print(evennumbers)
print(oddnumbers)

mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 == 0)]
oddnumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 != 0)]
print(mynumbers)
print(evennumbers)
print(oddnumbers)

shirtcolors = ["White", "Red", "Blue"]
pantcolors = ["Black", "Brown", "Blue"]
combinations = []
for shirtcolor in shirtcolors:
    for pantcolor in pantcolors:
        if (shirtcolor != pantcolor):
            combinations.append((shirtcolor, pantcolor))
print(combinations)

print("\n")

combinations = [(shirtcolor, pantcolor) for shirtcolor in shirtcolors for pantcolor in pantcolors if (shirtcolor != pantcolor)]
print(combinations)

mynumbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iseven = True
for mynumber in mynumbers:
    if (mynumber % 2 != 0): iseven = False
if (iseven):
    print("All items are even numbers")
else:
    print("Some items are not even numbers")

# all functions takes list of boolean values
# and checks whether all the vallues are True
# if all are True then it returns True
if all([(mynumber % 2 == 0) for mynumber in mynumbers]):
    print("All items are even numbers")
else:
    print("Some items are not even numbers")

# any function takes list of boolean values
# and checks whether any True is available
# if one True  is there then it return True (or operator)

# swap number
x = 10
y = 15
x, y = y, x
print(x, y)

# We process list and we get a new list
# Overhere the number of items in the original list and newly created list
# are always same
celciusvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# using traditional for loop
fahrenheitvalues = []
for celciusvalue in celciusvalues:
    fahrenheitvalues.append((celciusvalue * 9 / 5) + 32)
# using list comprehension
fahrenheitvalues = [((celciusvalue * 9/5) + 32) for celciusvalue in celciusvalues]
# we can also solve this type of problems using map function
# map is a built in function that is an alternative to for loop
def convertCelciusToFahrenheit(celciusvalue):
    return (celciusvalue * 9/5) + 32
fahrenheitvalues = map(convertCelciusToFahrenheit, celciusvalues)
# map object is an iterable object
# however print functionn do not how to iterate the map object
# so we typecast map function to a list so that print can print the valuesd
print(list(fahrenheitvalues))

# We process list and we get a new list
# Overhere the number of items in the original list and newly created list
# is less than or equals to the number of items in the original list
mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filter the even numbers only
evennumbers = []
for mynumber in mynumbers:
    if (mynumber % 2 == 0):
        evennumbers.append(mynumber)
# use list comprehension
evennumbers = [mynumber for mynumber in mynumbers if (mynumber % 2 == 0)]
# this type of proble,s can be solved using built in function called filter
# You need to create a function that returns Trus or False
# Function that returns True or Fase is also called "Predicate function"
def isEven(number):
    return number % 2 == 0
evennumbers = filter(isEven, mynumbers)
print(list(evennumbers))

# We process list and we get a single value
# Over here, we are reducing our list to a single value
# python has many built in modules
# one such module is functools
from functools import reduce
mynumbers = [1, 2, 3, 4, 5]
# to add 2 items let us create a function
def add(previousvalue, currentvalue):
    # note the reduce function is smart
    # when we use + the previous values is initialized with 0
    # when we use * the previous values is initialized wih 1
    # however you can configure the initial value for the previous value
    return previousvalue * currentvalue
result = reduce(add, mynumbers, 2)
print("Result:", result)