# # Take age as input
# # age less than 10 is children
# # age greater than or equals to 10 and less than 18 is minor
# # age greater than or equals to 18 and less than 21 is Teenager
# # age greater than or equals to 21 and less than 60 is adult
# # age greater than or equals to 60 and above is Senior

# age = int(input("Input your age: "))
# if (age < 10):
#     print("Age", age, "is a child")
# elif (age >= 10 and age < 18):
#     print("Age", age, "is a minor")
# elif (age >= 18 and age < 21):
#     print("Age", age, "is a teenager")
# elif (age >= 21 and age < 60):
#     print("Age", age, "is an adult")
# else:
#     print("Age", age, "is a senior")

# print("Children") if (age < 10) \
#     else print("Minor") if (age >= 10 and age < 18) \
#     else print("Teenager") if (age >= 18 and age < 21) \
#     else print("Adult") if (age >= 21 and age < 60) \
#     else print("Senior")

# Using arithmetic expression in shorthand if syntax
# So far we always call print function which does not return anything
# now we want to see how to use arithmetic expression which returns value
op = "+"
x = 10
y = 5
# let us create a simple calculator using if syntax
result = x + y if (op == "+") \
    else x - y if (op == "-") \
    else x * y if (op == "*") \
    else x / y

# same is applicable for function call
op = "A"
x = "Television"
result = id(x) if (op == "A") \
    else type(x) if (op == "D") \
    else len(x)