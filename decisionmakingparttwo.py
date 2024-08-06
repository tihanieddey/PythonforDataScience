# soo far we have seen how to handle
# single condition and single condition with else part
# In real world you may have too handle multiple condition
# one after another, or we can call it as nested conditions

# Identify whether the given number is positive, negative
# or zero

# givennumber = 10
# if (givennumber > 0):
#     print("Given number is positive")
# else:
#     if (givennumber == 0):
#         print("Given number is zero")
#     else:
#         print("Given number is Negative")

# givennumber = 0
# if (givennumber >= 0):
#     if (givennumber == 0):
#         print("Given number is zero")
#     else:
#         print("Given number is positive")
# else:
#     print("Given number is Negative")

# # Let us do it using elif
# givennumber = 0
# if (givennumber > 0):
#     print("Given number is positive")
# elif (givennumber == 0):
#     print("Given number is zero")
# elif (givennumber < 0):
#     print("Given number is Negative")

givennumber = 0
if (givennumber > 0):
    print("Given number is positive")
elif (givennumber == 0):
    print("Given number is zero")
else:
    print("Given number is Negative")