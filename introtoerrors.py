# Name Error
# the variable must be defined and initialised
# before we use it (access it)
# print(name) # Name Error : name 'step' is not defined
# step = step + 1 # Name Error: name 'step' is not defined
 
# Type Error
# len is a built in function  that can tell us how many characters
# we have in a string
# myname = "Jegan"
# print(len(myname))
# # this function is expecting you to send a string 
# # but what if you send a number
# print(len(42)) # TypeError: object of type 'int' has no len()
# x = "10"
# y = 5
# z = x - y # TypeError: unsupported operand type(s) for -: 'str' and 'int

# # Value Error
# # int function will convert string to integer
# # the function is expecting you to send "string"
# print(int(10)) # still work
# print(int(True)) # still work
# print(int("apple")) # ValueError: invalid literal for int() with base 10: 'apple'
# print(int("a")) # ValueError: invalid literal for int() with base 10: 'a'

# # Syntax Error
# # rules while programming
# # when we call the function, function name must be followed by ()
# print"Hello" # SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?