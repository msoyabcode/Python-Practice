# Create a list of 5 numbers and find their sum.

# list = [1, 2, 3, 4, 5]

# total = 0

# for i in list:
#     total+=i

# print(total)


# Find the largest number in a list.
# list = [1, 2, -1, 3, 4, 5]

# largestNum = list[0]

# for i in list:
#     if i>largestNum:
#         largestNum = i

# print(largestNum)


# Find the smallest number in a list.
# list = [1, 2, -1, 3, 4, 5]

# smallestNum = list[0]

# for i in list:
#     if i<smallestNum:
#         smallestNum = i

# print(smallestNum)


# Count how many even and odd numbers are present in a list.
# lst = [1, 2, 3, 4, 5, 6]
# evenCount = 0
# oddCount = 0

# for i in lst:
#     if i%2==0:
#         evenCount+=1
#     else:
#         oddCount+=1

# print(evenCount)
# print(oddCount)



# # Remove duplicate values from a list.
# lst = [1, 2, 1, 23, 1, 2, 23, 1, 2, 3, 4, 5, 6]

# nonDuplicateList = []

# for i in lst:
#     if i not in nonDuplicateList:
#         nonDuplicateList.append(i)
    
        

# print(nonDuplicateList)






# Reverse a list without using the reverse() method.
# lst = [1,2,3,4,5]

# # lst.reverse()
# # print(lst)

# reverseList = []

# for i in range(len(lst) -1, -1, -1):
#     reverseList.append(lst[i])

# print(reverseList)




# Find the second largest number in a list.

# lst = [1,2,9, 2, 4,5]

# largestNum = 0
# secondLargestNum = 0

# for i in lst:
#     if i>largestNum and i>secondLargestNum:
#         secondLargestNum = largestNum
#         largestNum = i

#     elif i>secondLargestNum and i<largestNum:
#         secondLargestNum = largestNum

# print(f"largest number: {largestNum}")
# print(f"second Largest number: {secondLargestNum}")



# Create two lists and combine them into one list
# lst1 = [1,2,3]
# lst2 = [1,2,3,4,5,5]
# lst1.extend(lst2)
# print(lst1)




# Check whether a particular element exists in a list.
# lst = [1, 2, 3, 5, 6]

# if 3 in lst:
#     print("yes, 3 is in the list")

#     # or

# for i in lst:
#     if i == 3:
#         print("yes 3 is in list")