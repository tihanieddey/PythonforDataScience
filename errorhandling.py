# # When ever you have inputs
# # the input can be keyboard, files, database or even network api call
# # There is a high chance for a runtime error to happen in future
# # To handle the runtime they have try except block in Python
# try:
#     # the code that may cause problem in the future must be placed here
#     principle = int(input("Enter principle amount (RM): "))
# except:
#     # the code that gets executed when an error occurs
#     print("Principle amount must be just a number")
# else: # optional
#     # the code that gets executed when no error occurs
#     print("Principle amount is ok")
#     # pass # to tell python I will add the code here but later
# finally: # optional
#     # the code that always gets executed 
#     # regardless of whether an error occur or no error occur
#     print("Thank you")

# period = int(input("Enter the period in years: "))
# rate = int(input("Enter the interest rate(%): "))
# interest = (principle * period * rate) / 100
# print("Interest: ", interest)

# However the previous example does not ensure the principle amount is a number
isErrorInput = True
while(isErrorInput):
    try:
        principle = int(input("Enter the principle amount: "))
    except:
        print("Principle amount must be number")
    else:
        isErrorInput = False
# print("Principle Amount: ", principle)
period = int(input("Enter the period in years: "))
rate = int(input("Enter the interest rate(%): "))
interest = (principle * period * rate) / 100
print("Interest: ", interest)