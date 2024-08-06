# # We need loops for the following:
# # 1) We have to iterate through a list/tuple/any iterable object
# # 2) To handle repeated code (copy paste block of code) base on some condition

# # In python the developers are very clear about these objectives so they
# # create just 2 loop structures
# # to handle the first problem use for loop
# # to handle the second problem use while loop

# fruits = ["apple", "orange", "mango", "banana", "grapes"]
# # for fruit in fruits:
# #     print(fruit)

# # # we know + sign is a overloaded operator (arithmetic addition, string concatenation)
# # # similarly * sign is also an overloaded operator
# # # string can be multiplied with an integer (time operator)
# # print("=" * 80) # it is going to print the = 80 times
# separator = ("=" * 80)
# print(separator)

# # print fruit with 6 letters
# for fruit in fruits:
#     if (len(fruit) == 6):
#         print(fruit)

# # In other programming languages we will put out the items from a list (array)
# # using index for (i = 0; i < array.size; i++) array[i]
# # Sometimes you may want to pull the item together with index
# # There is a built in function called range
# # range will take start index and end index (end index is not included)
# indexes = range(0, len(fruits)) # please generate numbers from 0 to 5 (5 not included)
# print(indexes)
# # range is also an iterable object like this
# # however print function do not know how to iterate the range subject
# # we still can typecast the range object to a list object
# # since range is an iterable object
# print(list(indexes))
# # however this typecasting is not require when we use the iterable object in for loop
# for index in range(0, len(fruits)):
#     print(index + 1, fruits[index])

# # there is also another function called enumerate
# # this enumerate function takes iterable object as argument
# # and returns "list of tuples" and each tuple will have index and value
# print(enumerate(fruits))
# # print is not able to iterate the enumerate object
# print(list(enumerate(fruits)))
# for index, value in enumerate(fruits):
#     print(index, value)

# print(list(range(0, 101, 25)))

# # Only in python for loop also has else part
# # the code in the else part will get executed
# # if all the items in the list is iterated successfully
# # in other words the loop is exhausted with the list
# fruits = ["apple", "orange", "mango", "banana", "grapes"]
# for fruit in fruits:
#     print(fruit)
# else:
#     print("All fruits printed successfully")

# for fruit in fruits:
#     #  break is a keyword which will bring me out of the for loop
#     if(fruit == "mango"): break
#     print(fruit)
# else:
#     print("All fruits printed successfully")

# mynumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for mynumber in mynumbers:
#     if mynumber % 2 != 0: continue
#     # continue keywords continues the loop without executing
#     # the following statements
#     print(mynumber)

# ========================================================================

# When to use while loop
# 1) You do not have a list
# 2) You do not know how many time to repeat
# 3) However, you have a condition to terminate

# # Create a multiplication table of 5
# # 1 x 5 = 5
# # 12 x 5 = 60
# # for multiplier in range(1,13)
# num = 0
# n = 0
# while (n < 13):
#     num = n * 5
#     n += 1
#     print(num)

# reverse the number
givenNumber = int(input("Enter the number: "))
result = 0
while (givenNumber > 0):
    result = result * 10 + (givenNumber % 10)
    givenNumber = givenNumber // 10
else:
    # the code in the else part will get executed 
    # only when the condition returns false
    # in this case givenNumber must be less than or equals to 0
    print(result)