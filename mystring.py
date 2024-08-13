# String literals are enclosed with double quote or
# single quote
message = "Hello World"
message = 'Hello World'
# In python actually no difference
# Here message is a string object
# which means message object will have many methods
# for example upper method will convert all characters to capital letter
print(message.upper()) # not inline
# inline means do the changes and assign the changed value to the same variable
print(message)
# it is your responsible to capture the uppervalue into a variable and print it
uppermessage = message.upper()
print(uppermessage)

print(message.lower())
print(message.capitalize())

print("JCG" + " " + str(8949))

carplate = "JCG"
number = 8949
carplatenumber = f"{carplate:4s}{number}" # f"{carplate}{" "}{number}"
print(carplatenumber)

# escape sequences
# \n new line
# \t tab key
# \r carriage return
filepath = "c: \newfolder\table\report.txt"
print(filepath)
filepath = "c: \\newfolder\\table\\report.txt"
print(filepath)
# raw string
filepath = r"c: \newfolder\table\report.txt"
print(filepath)

# multiline strings
# it can be created using 3 double quote or 3 single quote
mystring =  """Paris, France's capital, is a major European city and a global center for art, fashion, gastronomy and culture. 
Its 19th-century cityscape is crisscrossed by wide boulevards and the River Seine."""

# paragraph can be converted into list of words
words = mystring.split()
print(words)
print(len(words))

# how to remove all the spaces in the string
# find the space and replace it with no space
print(mystring.replace(" ", ""))
print(mystring.replace("a", "aaaaaaa"))

print(mystring.count("a "))

mystring = "I bought {0:5d} {1:20s} for RM{2:10.2f}"
print(mystring.format(10, "Television", 1455.55))
print(mystring.format(11, "Radio", 657.25))

print(words)

print("--------".join(words))

mystring = "Hello welcome to Python \n"
print(mystring.strip(), "123", sep = "") #strip has remove " \n"
print(mystring.strip())
# we can safely say strip removes all the escape sequences 
# at the end of the string
# and also the spaces at the beginning and end of the string