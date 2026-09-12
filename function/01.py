# Create a function that takes two numbers and returns their sum.

# def add_numbers(a, b):
#      return a+b

# result = add_numbers(3,2)
# print(result)



# Create a function that checks whether a number is even or odd.
# def even_or_odd(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"

# rslt = even_or_odd(2)
# print(rslt)




# Create a function that finds the largest number between two numbers.

# def largest_num(a,b):
#     if a>b:
#         return f"the largest number is a = {a}"
#     else:
#         return f"the largest number is b = {b}"

# a= 3
# b= 9

# rsl = largest_num(a, b)
# print(rsl)




# Create a function that calculates the factorial of a number.

# def factorial(num):
#     result = 1

#     for i in range(num, 0, -1):
#         result *= i

#     return result


# num = 5
# answer = factorial(num)

# print(f"Factorial of {num} is {answer}")


# def factorial(num):
#     result = 1
#     i = num

#     while i > 0:
#         result *= i
#         i -= 1

#     return result


# num = 5
# answer = factorial(num)

# print(f"Factorial of {num} is {answer}") 



# Create a function that counts vowels in a string.
# def count_Vowels(str):
#     count = 0

#     for i in str:
#         if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
#             count+=1
#     return count

# result = count_Vowels("hello i am soyab")
# print(result)


# def count_Vowels(str):

#     count = 0
#     i = 0 

#     while i<len(str):
#         if  str[i] in "aeiou":
#          count+=1
#         i+=1

#     return count


# result = count_Vowels("hello i am soyab")
# print(result)




# Create a function that reverses a string.
# def reverse_string(str):
#     reverse = ""
#     # for i in range(len(str)-1, -1, -1):
#     #     reverse+=str[i]

#     for char in str:
#         reverse=char+reverse

#     return reverse


# result = reverse_string("abc")
# print(result)


# def reverse_string(str):
#     reverse = ""
#     i = 0
#     while i<len(str):
#         reverse = str[i]+reverse
#         i = i+1

#     return reverse

# result = reverse_string("abc")
# print(result)



# Create a function that checks whether a string is a palindrome.
# def palindrome_check(text):
#     reverse = ""
#     i = 0
#     while i<len(text):
#         reverse =text[i]+reverse
#         i = i+1

#     if reverse==text:
#         return "it is palindrome"
#     else:
#         return "it is not palindrome"

# result = palindrome_check("madam")
# print(result)



# def palindrome_check(text):
#     reverse = ""

#     for index in text:
#         reverse = index+reverse

#     if reverse == text:
#         return "palindrome"
#     else:
#         return "not palindrome"

# result = palindrome_check("madam")
# print(result)



# Create a calculator function that performs:


def calculator(a,b, operator):

    if operator == "add":
        return a+b
    elif operator == "subtract":
        return a-b
    elif operator == "multiply":
        return a*b
    elif operator == "devide":
        return a/b
    else:
        return "Invalid operator"  

result =  calculator(3, 3, "multiply")
print(result)
