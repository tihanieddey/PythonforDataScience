# # So far we have learn how to assign a single value to a single variable
# # product = "Television"
# # We also know we can assign multiple values to multiple variables
# # product, quantity, price = "Television", 10, 1455.55, 55

# # Today let us discuss how to assign multiple values to a single variable
# fruits = ["apple", "orange", "mango", "banana", "grapes"]
# # the above is called list in python
# # we use [] to create a list

# # you can pass the list to the print function and it can
# # iterate through the list and print all the items inside list
# print(fruits)

# # List allows dupllicates
# fruits = ["apple", "orange", "apple", "mango", "banana", "apple", "grapes"]
# print(fruits)

# # List is ordered (the item inside the list retain its position)
# # How do they maintain the order ?
# # List in python has index (created by python internally)
# # The index starts with 0 
# # The maximun index is nothing but (totalnumberofitems - 1)
fruits = ["apple", "orange", "mango", "banana", "grapes"]
# print(fruits[0]) #Apple
# print(fruits[1]) #Orange
# print(fruits[2]) #Mango
# print(fruits[3]) #Banana
# print(fruits[4]) #Grapes

# # Index numbers can also be negative
# # -1 refers to the last item in the list
# print(fruits[-1]) # grapes
# print(fruits[-2]) # banana
# print(fruits[-3]) # mango
# print(fruits[-4]) # orange
# print(fruits[-5]) # apple

# # we can also slice a list
# # : is a range operator
# # first number is used as start index, second number is used as end index
# # however end index is not included
# slice = fruits[1:3] #banana is not listed
# print(slice)
# slice = fruits[1:4] #banana is listed
# print(slice)
# # If you want the last item then you have to use the maximum index + 1
# # Remember this is only in Range
# slice = fruits[1:5] #last item is printed
# print(slice)
# # If you have some kind of pattern then we can pull out the items 
# # Indexes divisible by 2
# slice = fruits[0:5:2] #the third parameter for the range is step up
# print(slice)
# slice = fruits[:4] #since start index is missing it will start from 0
# print(slice)
# slice = fruits[2:] #since end index is missing it will start from 2 and go all the way to the last item
# print(slice)
# # Can we use negative index in the range=> Definitely can
# # make sure start indes is < than end index
# slice = fruits[-4:-1] # it is not reversed
# print(slice)
# # Usage of negative step up value
# slice = fruits[-1:-5:-1] # it is reversed
# print(slice)
# slice = fruits[::-1] # it is fully reversed
# print(slice)
# # len function is also used to find the number of items in the list
# print(len(fruits))

# # What we understand is string is nothing but a list of characters
# message = "Welcome to python programming"
# print(message[11:17])

# fruits = ["apple", "orange", "mango"]
# newfruits = ["apple", "orange", "mango"]
# print(id(fruits))
# print(id(newfruits))

# # this is not real copy referring to the same memory location
# oldfruits = fruits
# fruits[0] = "Durian"
# print(oldfruits)
# print(fruits)

# # ======================================================================
# # 5 / 8 / 2024

# # Similar to lists we also have another data structure called tuple
# # Tuple is nothing but read only list
# # Tuple use ()
# countries = ("Malaysia", "Singapore", "Thailand", "Indonesia", "Vietnam")
# # Tuple is also ordered and index same as list
# # Only thing that cannot be done is changes
# # we cannot add a new country we cannot remove a country we cannot modify a country
# print(countries)
# # Again print function knows how to iterate through the tuple and print
# # the values inside the tuple
# # Indexing is exactly same as LIST
# print(countries[0])
# print(countries[-2])
# print(countries[1:4])
# # Performance wise, tuple is faster than list
# # When you perform analysis its good to use tuple rather than list
# # Python's preferred data structure is "tuple"
# # If you ask any python function which returns more than 1 value it always returns
# # tuple instead of list
# # When ever you pass a list as an argument it is preferred to pass it as tuple
# # if the function try to modify the values inside the tuple python will immediately
# # throw error
# # sum([10, 20, 30, 40, 50]) # you can pass list as an argument like this (here, we are passing  1 argument)
# # sum(10, 20, 30, 40, 50) # they are totally different (here we are passing 5 arguments)
# # sum((10, 20, 30, 40, 50)) # Instead of list send it as tuple

# # This () is used in many places
# # In arithmetic expression was used to give high priority y = a * (b + c)
# # function() => To call a function we use () immediately after the function name
# # In tuple also we use (10, 20, 30, 40, 50)

# # # Typecasting this will convert iterable object to a list
# # countrieslist = list(countries)
# # print(countrieslist)
# # print(type(countrieslist))
# # countriestuple = tuple(countrieslist)
# # print(countriestuple)
# # print(type(countriestuple))

# # print(isinstance(countrieslist, list))

# # mynumbers = [10]
# # print(mynumbers, type(mynumbers))

# # mynumbers = (10,) # add an extra comma to retain its tuple feature
# # print(mynumbers, type(mynumbers))

# # if a function call suppose to return tuple and one good day
# # the function returns a single value, then it becomes integer
# # If you try to pull the items using [] it will throw runtime error

# # the list and tuple can unpack the items into individual wariables automatically
# studentdetail = ["Khairi", "Abu Bakar", 920102121234, 2450.25]
# # In a traditional programming languages
# firstname = studentdetail[0]
# lastname = studentdetail[1]
# icnumber = studentdetail[2]
# amounttobepaid = studentdetail[3]
# print(firstname, lastname, icnumber, amounttobepaid)

# # But in python you just need to do this
# fname, lname, ic, amount = studentdetail
# print(fname, lname, ic, amount)

# studentdetails = [
#     ("Khairi", "Abu Bakar", 920102121234, 2450.25),
#     ("Peter", "Parker", 940102124544, 4356.25),
#     ("Chan", "Wai Foo", 930102124544, 1356.25)
# ]

# print(studentdetails)

# for studentdetail in studentdetails:
#     print(studentdetail) #tuple

# for fname, lname, ic, amount in studentdetails:
#     print(fname, lname, ic, amount)

# ===========================================================================
# 6 / 8 / 2024

fruits = ["apple", "orange", "mango"]
# methods are nothing but functions inside and object
# to call a method, first you must have the object
# here fahrenheitvalues is the list object
# to call the method inside the list object we will use the dot (.) operator
# which is followed by the function name
fruits.append("grapes")
# fruits.extend(["durian", "rambutan"])
fruits.extend(["durian", "rambutan"])
print(fruits)

x = [10, 20, 30, 40, 50]
y = [60, 70, 80, 90, 100]
z = x + y
print(z)

print(fruits)
# Let us insert a fruit in a particular index
# insert is a method inside the list object
# fruits is a list object
fruits.insert(2, "banana")
print(fruits)
fruits.insert(5, "pineapple")
print(fruits)
# print(len(fruits))

# Let us delete a fruit in a particular index
# remove is a method inside the list object
# fruits is a list object
fruits.remove("mango")
print(fruits)

# Delete an item by index
# We do not have a method to handle this
# But we can use the del keyword to delete the item
# del is a very powerful keyword in python
# which deletes anything from memory immediately, permanently
del fruits[1]
print(fruits)

# fruits[1] = "mango"
# print(fruits)

# you can also delete the entire list
del fruits

fruits = ["apple", "orange", "mango", "banana", "grapes", "durian", "rambutan", "cempedak"]
fruits.clear()
print(fruits)

fruits = ["apple", "orange", "mango", "banana", "grapes", "durian", "rambutan", "cempedak"]
# localfruits = fruits #this will create a shallow copy
# both variables will point to the same location
# you have to use loop or list comprehension and copy a list into another list
# An easy approach is use the copy method
localfruits = fruits.copy()
print(fruits)
print(localfruits)
fruits.append("pineapple")
print(fruits)
print(localfruits)

# the following statement will help you to find out how many apple we have
# in the list
print(fruits.count("apple"))

# the following statement will help you to find out the index of durian
# in the list
print(fruits.index("durian"))

# pop will remove the last item in the list
fruits.pop()
print(fruits)

# sort by ascending order
fruits.sort()
print(fruits)

# sort it by descending order (inline)
fruits.reverse() # you loose the original ordering
# if you want to maintain the original order then copy first
print(fruits)

fruits = ["apple", "orange", "mango", "banana", "avocado", "grapes"]
fruits.sort()
print(fruits)