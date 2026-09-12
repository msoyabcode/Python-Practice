# Print numbers from 1 to 10 using a loop.

# for i in range(1, 10):
#     print(i)

# or

# i = 1
# while i<=10:
#   print(i)
#   i+=1




# Print all even numbers between 1 and 50.
# for i in range(1, 51):
#     if i%2 == 0:
#         print(i )

# i = 1
# while i<=50:
#     if i%2 == 0:
#         print(i)
#     i+=1



 # Print the multiplication table of a number.
# num = int(input("Enter number: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

# i = 1
# while i<=10:
#     print(f"{num} x {i} = {num*i}")
#     i+=1
    

    # Find the sum of numbers from 1 to 100.
# sum = 0
# for i in range(1, 101):
#     sum =  sum + i

# print(sum)

# sum = 0
# i = 1
# while i<=100:
#     sum = sum + i

#     i+=1

# print(sum)




# Calculate the factorial of a number.
# num = int(input("Enter number: "))

# factorial = 1

# for i in range( num, 0, -1):
#     factorial*=i

# print(factorial) 


# total = 1
# i = num
# while i>=1:
#     total = total *i
#     i = i-1

# print(total)



# Count the number of digits in a number.
# num = int(input("Enter number: "))

# total = 0
# for i in str(num):
#     total = total+1
# print(total)

# num = int(input("Enter number: "))

# count = 0

# while num > 0:
#     num = num // 10
#     count += 1

# print(count)




# Reverse a number.
# st = str(num)

# for i in range(st, len(st)-1, -1):
#     print(i)

# num = int(input("Enter number: "))

# reverse = 0

# while num>0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print(reverse)

# num = int(input("Enter number: "))
# str = str(num)

# reverse = ""
# for i in range(len(str)-1, -1, -1):
#     reverse = reverse+str[i]


# print(reverse)





# Check whether a number is a palindrome.

# num = int(input("Enter number: "))

# str_num = str(num)

# reverse = ""

# for i in range(len(str_num)-1, -1, -1):
#     reverse = reverse + str_num[i]

# if str_num == reverse:
#     print(f"{str_num} is a palindrom")

# else:
#     print(f"{str_num} is not a palindrom")


num = int(input("Enter number: "))
original = num
reverse = 0
while num>0:
    last_dgt = num % 10
    reverse = reverse*10+last_dgt
    num = num //10

if original == reverse:
    print("palindrom")

else:
    print("not palindrom")
