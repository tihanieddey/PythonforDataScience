product = "Television"
quantity = 10
price = 1455.55
isAvailable = True

# % operator is also overloaded (which means there are also other use of it)
result = "I bought %s today. I bought %d for %.2f total in RM" % (product, quantity, price)
print(result)

# formatted strings are also called f-strings

print("=" * 35)
result = f"{product:20s}{quantity:5d}{price:10.2f}"
print(result)
print(f"{product:>20s}{quantity:<5d}{price:^10.2f}")
print(result)
print("=" * 35)