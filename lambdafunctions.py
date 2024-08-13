# anonymous function: function without name
# If there is function without name how to call them?
# Normally when we talk about anonymous function in other
# programming languages they are talking about creating 
# the function body in memory and holding the address
# location in a variable where the function body is

# # normal function
# def sayHello():
#     print("Hello")

# # anonymous function
# def ():
#     print("Hello")

# # anonymous function assigned to a variable
# sayHello = def ():
#     print("Hello")

# # calling the variable indirectly the functionn gets executed
# sayHello()

# Before we start exploring the lambda functionn let us try to 
# understand its drawback.
# lambda function in python can have single line of statement only
# Lambda function is nothing but anonymous functionn assigned to
# a variable instead of using def, you can use the keyword lambda
sayHello = lambda: print("Hello")

sayHello()

# def square(x):
#   return x ** 2

# brackets over the parameters are not necessary
# return keyword is also not necessary
square = lambda x: x **2
print(square(3))

# def simpleInterest(principle, period, rate):
#   return (principle * period * rate) / 100

simpleinterest = lambda principle, period, rate: (principle * period * rate) / 100
print(simpleinterest(1000, 1, 6))