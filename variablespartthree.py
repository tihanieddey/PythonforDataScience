# ser uses {}
# set is not indexed
# set is not ordered
fruits = {"apple", "orange", "mango", "banana", "durian"}
print(fruits)

# print(fruits[0]) # cannot use index, not subscriptable

# however it is iterable
for fruit in fruits:
    print(fruit)

# More than one item assigned to a single variable is called "Iterable Object"
# Not all Iterable objects are "Subscriptable"

# set does not allow duplicates
fruits = ["apple", "orange", "mango", "banana", "apple", "grapes", "apple", "durian"]
print(fruits)
# you can always typecast any iterable object to a set using set function
fruitset = set(fruits)
print(fruitset)

# We cannot append (adding as last item) an item, since it is not indexed
# However we can add a new item to the existing set
fruitset.add("rambutan")
print(fruitset)

# Can I remove an existing item
fruitset.remove("apple")
print(fruitset)

# You can also remove an item randomly using pop method
fruitset.pop()
print(fruitset)

# you can clear all the items inside the set
fruitset.clear()
print(fruitset) # the empty set is printed as "set()" because {} is also used by dictionary

# what if I want to add more than one from to the set
fruitset = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"cempedak", "mangosteen", "grapes"}
fruitset.update(localfruits)
print(fruitset)

print("=" * 80)

# Set Arithmetic
localfruits = {"cempedak", "mangosteen", "banana", "durian", "rambutan"}
overseafruits = {"apple", "orange", "mango", "grapes", "banana"}

# Let us get all fruits
allfruits = localfruits.union(overseafruits)
print(allfruits)
# Let us get fruits which are available locally and in oversea
commonfruits = localfruits.intersection(overseafruits)
print(commonfruits)
# Let us get fruits which are available only in Malaysia
malaysianfruits = localfruits.difference(overseafruits)
print(malaysianfruits)
# Let us get fruits which are totally not in Malaysia
importedfruits = overseafruits.difference(localfruits)
print(importedfruits)

favoritefruits = {"durian", "rambutan", "mangosteen"}
# whether all my favorite fruits are available locally
print(favoritefruits.issubset(localfruits))
# whether locally available fruits are superset of my favorite fruits
print(localfruits.issuperset(favoritefruits))

# that means my favorite fruits is totally disjoint with oversea fruits
print(favoritefruits.isdisjoint(overseafruits))

# Get me all the fruits but minus the fruit which is available in both places
print(localfruits.symmetric_difference(overseafruits))

# find the result and update the localfruits with result (then use update)
# careful you going to loose the data in localfruits
localfruits.intersection_update(overseafruits)
print(localfruits)

# set is a function that help us to create set object
# similarly frozen_set is another built in function that help us to create read only set object
# this is similar to list (modifiable) and tuple (read only list)
# this is similar to set (modifiable) and frozenset (read only list)
readonlyset = frozenset({"apple", "orange", "mango", "banana"})
print(readonlyset)