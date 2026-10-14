# Write a recursive function to print numbers from 1 to 10.

# def print_numbers(n):

#     if n>10:
#         return # base condition or stop condition

#     print(n)

#     print_numbers(n+1) # recursive case function call itself

# print_numbers(1)



# # Write a recursive function to calculate factorial.
# def factorial_calculate(num):
#     if num==0:
#         return 1

#     return num * factorial_calculate(num-1)

# result = factorial_calculate(5)
# print(result)
    



# Write a recursive function to calculate the sum of numbers from 1 to n.

# def sum(n):
#     if n==0:
#         return 0

#     return n+sum(n-1)

# result = sum(3)
# print(result)



# Write a recursive function to calculate the power of a number.
# def power_find(base, power):

#     if power == 0:
#         return 1

#     return base*power_find(base, power-1)


# result = power_find(2, 2)
# print(result)



# Write a recursive function to reverse a string.
# def reverse_string(text):

#     if text == "":
#         return  ""

#     return text[-1] + reverse_string(text[:-1])

# result = reverse_string("abc") e
# print(result)


# Write a recursive function to calculate Fibonacci numbers.
# def febonacci_sum(num):

#     if num == 0:
#         return 0

#     if num == 1:
#         return 1

#     return febonacci_sum(num-1)+febonacci_sum(num-2)

# result = febonacci_sum(6)
# print(result)



# Find the sum of digits of a number.
# num = input("Enter number: ")

# total = 0

# for i in num:
#     total+=int(i)

# print(total)


# Find the largest digit in a number.
num = input("Enter number: ")
# print(num)

largest  = 0

# for i in num:
#     if int(i)>largest:
#         largest = int(i) 

# print(largest)
i = 0 
while i<len(num):
    if int(num[i])>largest:
        largest = int(num[i])

    i+=1
print(largest)