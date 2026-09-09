
# Take a string from the user and print its length.

# str = input("enter string: ")
# print(len(str))




# Count how many vowels are present in a string.
# string = input("Enter string: ")

# count = 0
# for i in string:
#     if( i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#         count = count+1

# print(count)



# Reverse a string.
# string = input("Enter string: ")
# reverse = ""
# for i in range(len(string) -1, -1, -1):
#     reverse = reverse+string[i]

# print(reverse)




# Check whether a string is a palindrome.

# string = input("Enter string: ")
# revers = ""
# for i in range(len(string) -1, -1, -1):
#     revers+=string[i]

# if(string == revers):
#     print(f"{string} is a palindrome")

# else:
#     print(f"{string} is not palindrome")





# Count how many times a particular character appears in a string.
# string = input("Enter string: ")
# char = input("Enter character: ")

# print(string.count(char))

# or
#  
# count = 0
# for i in string:
#     if(i==char):
#         count+=1

# print(count)




# Convert the first letter of every word into uppercase.
# string = input("Enter string: ")
# print(string.title())


# # Remove all spaces from a string.
# string = input("Enter string: ")
# print(string.replace(" ", ""))


# User se ek sentence lo.
# Sentence mein multiple words honge.
# Tumhe har word ko ek-ek karke check karna hai.
# Har word ki length compare karni hai.
# Ek variable mein ab tak ka largest word store karna hoga.
# Agar current word ki length stored largest word se zyada ho, to largest word update kar do.
# End mein largest word print karo.
# Find the largest word in a sentence.
string = input("Enter string: ")
largestWord = " "

for i in string.split():
    if len(i) > len(largestWord):
        largestWord = i

print(largestWord)