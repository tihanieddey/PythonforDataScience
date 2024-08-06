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