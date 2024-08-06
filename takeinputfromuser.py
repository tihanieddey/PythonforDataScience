# Python has a built in function called input
# it takes a single parameter which is the caption
# It always returns the input as string

yourname = input("What is your name: ")
# by default, print function will print everything with space
# you can change the behaviour by adding a keyword argument
# the keyword is sep and the value is "" (empty)
# print("Hello ", yourname, ", Good morning")
print("Hello ", yourname, ", Good morning", sep="")
print("Data type of the input is always string: ", type(yourname))

# Let us calculate simple interest
# interest = (principle * rate * period) / 100
principle = float(input("Enter Amount  (RM): "))
period = float(input("Enter the year: "))
rate = float(input("Enter rate (%): "))
interest = (principle * period * rate) / 100 
print("Interest amount: ", interest)
print("Total amount to be paid: ", principle + interest)