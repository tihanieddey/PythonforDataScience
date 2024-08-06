# Find the biggest digit in the given number 78693

# number = 78693
# temp = 0
# result = 0

# # Solution 1

# temp = number // 10000
# # print(temp)
# if (temp > result):
#     result = temp
# # print(result)
# temp = (number // 1000) % 10
# # print(temp)
# if (temp > result):
#     result = temp
# # print(result)
# temp = (number // 100) % 10
# # print(temp)
# if (temp > result):
#     result = temp
# # print(result)
# temp = (number // 10) % 10
# # print(temp)
# if (temp > result):
#     result = temp
# # print(result)
# temp = (number // 1) % 10
# # print(temp)
# if (temp > result):
#     result = temp
# print(result)

# #Solution 2

# temp = number % 10
# # print(temp)
# if(temp > result):
#     result = temp
# # print(result)
# number = (number // 10)
# # print(number)
# temp = number % 10
# # print(temp)
# if(temp > result):
#     result = temp
# # print(result)
# number = (number // 10)
# # print(number)
# temp = number % 10
# # print(temp)
# if(temp > result):
#     result = temp
# # print(result)
# number = (number // 10)
# # print(number)
# temp = number % 10
# # print(temp)
# if(temp > result):
#     result = temp
# # print(result)
# number = (number // 10)
# # print(number)
# temp = number % 10
# # print(temp)
# if(temp > result):
#     result = temp
# # print(result)
# number = (number // 10)
# # print(number)
# temp = number % 10
# # print(temp)
# if(temp > result):
#     result = temp
# print(result)

# # Solution 3
# while (number > 0):
#     temp = number % 10
#     print("This is the value for temp:", temp)
#     if(temp > result):
#         result = temp
#     print("This is the result:", result)
#     number = (number // 10)

# print("The biggest digit from number is ", result)