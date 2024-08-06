# # Arithmetic operators
# x = 20
# y = 10
# print(x + y) # addition
# print(x - y) # substraction
# print(x * y) # multiplication
# print(x / y) # division

# # 2 more operators
# x = 7
# y = 3
# print("Quotient: ", x // y)  
# print("Remainder", x % y) # modulus operator
# print(x / y)

# x = 2
# y = 3
# print(x ** y) # 2 to the power of 3

# # Assignment operators
# x, y , z = 10, 11 ,12
# print(x)
# print(y)
# print(z)

# #steps
# step = 0
# step = step + 1
# step = step + 1

# #steps (long leg)
# step  = 0
# step = step + 2
# step = step + 2
# #thers is a high chance for this guy to miss the floor
# #the first floor is at step 21

# step += 1 # step = step + 1
# step += 2 # step = step + 2
# step -= 1 # step = step - 1
# step -= 2 # step = step - 2
# step *= 1 # step = step * 1
# step *= 2 # step = step * 2

# step /= 1 # step = step / 1
# step //= 1 # step = step // 1
# step %= 1 # step = step % 1
# step **= 1 # step = step ** 1

# # Comparison Operators
# # Comparison operators always return TRUE or FALSE
# # Comparison operators help us to make decisions
# x = 10
# y = 15
# z = 10
# # Let us create comparisons that return TRUE
# print(x < y) # less than
# print(y > x) # greater than
# print(x != y) # not equals to
# print(x == z) # equals to
# print(x <= z) # less than or equals to
# print(x <= y) # less than or equals to
# print(y >= z) # greater than or equals to

# Logical Operators
# and, or, not --> Keywords in Python
# xor in python (^)
# Truth table
# print(condition1 AND condition 2)
# Condition 1               Condition 2             Result
# True                      True                    True
# True                      False                   False
# False                     True                    False
# False                     False                   False

# x = 10
# y = 5
# z = 8

# print((x > y) and (x > z))
# print((y < x) and (y < z))

# Truth table
# print(condition1 OR condition 2)
# Condition 1               Condition 2             Result
# True                      True                    True
# True                      False                   True
# False                     True                    True
# False                     False                   False

# x = 10
# y = 5
# z = 8

# print((x > y) or (x > z))
# print((y < x) or (y < z))
# print((y < z) or (x < y))
# print((x < y) or (x < z))

# Truth table for xor operator
# print(condition1 ^ condition 2)
# Condition 1               Condition 2             Result
# True                      True                    False
# True                      False                   True
# False                     True                    True
# False                     False                   False

# x = 10
# y = 5
# z = 8

# print((x > y) ^ (x > z)) # TRUE TRUE
# print((y < x) ^ (y > z)) # TRUE FALSE
# print((y < z) ^ (x < y)) # TRUE FALSE
# print((x < y) ^ (x < z)) # FALSE FALSE

# not operator also called as Negation Operator
# Negation means change True to False and False to True
# print(not (5 > 3))
# print(not (5 < 3))

# # Special Operators
# x = 101
# y = 101

# print(id(x))
# print(id(y))

# print(x == y) # comparison at value level
# print(x is y) # comparison at address level