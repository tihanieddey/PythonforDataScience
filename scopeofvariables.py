# main context
# the variable x will be in memory
# until the program gets terminated
x = 10
print(x)
x = None
print(x)
x = "Television"

def sayHello():
    # function context
    # local variable
    message = "Hello"
    print(message)
    
    # accessing the global variable inside the function
    # variable in the global context can be accessed 
    # inside the function context
    # print(x)

    # modifying the globale variable inside the function
    # what if we try to change the inside the function
    # when you try modify the variable in the global context 
    # python will quickly convert x to local variable
    # x = "Radio"
    # print(x)

    # How to modify the global variable inside the function
    # (intensionally)
    global x
    # Now we tell python always refer to the x declared in global
    x = "Radio"
    print(x)

# local variables cannot be accessed outside the function
# print(message)

# when the function gets invoked the code inside the function
# gets executed.
# The local variables are created during the code execution
# upon successfully completion of the function execution
# the local variables are destroyed
print(x)
sayHello()
print(x)

print("Thank you")

def outerfunction():
    # local variable belongs to outerfunction 
    outer = "Parker"
    def innerfunction():
        # local variable belongs to innerfunction
        # variable "inner" can be accessd only inside the innerfunction
        inner = "Peter"
        print(inner)

        # however I can access the variable which is in the outerfunction
        # inside the inner function
        # print(outer)

        # What will happen if I try to modify the variable in the 
        # outerfunction?
        # python will convert this to a local variable
        # outer = "John"
        # print(outer)

        # however what if I want to intentionally modify the variable
        nonlocal outer
        # Now we tell python always refer to the outer declared in outer function
        outer = "John"
        print(outer)

    # print(inner) # error
    print(outer)
    innerfunction()
    print(outer)

outerfunction()