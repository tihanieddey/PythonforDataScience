# # Is given number is positive ?
# x = 10
# # If (true): execute statement
# if (x >= 0):
#     print("Given number is positive")
# else:
#     print("Given number is negative")

# # The above syntax is suitable only if we have
# # single statement to be executed
# # But if you have more then 1 statement to be executed when the condition is True
# # then we have to create a "code block" (paragraph of statements)
# if (x > 0):
#     print("Given number is:", x)
#     print("Given number is positive")

# print("Thank you")

# Is the given number even or odd

x = 7
if (x % 2 == 0):
    print("Given number is:", x)
    print("Given number is even")
else:
    print("Given number is:", x)
    print("Given number is odd")

# What if I have only one statement to be executed for True
# and only one statement to be executed for False
print("Even") if (x % 2 == 0) else print("Odd")