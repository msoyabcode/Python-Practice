list = [34, 45, 34, 90, 80, 45 ,2 ]

largest = list[0]
smallest = list[0]

for i in list:
    if i > largest:
        largest = i
    elif i < smallest:
        smallest = i


print (largest)
print(smallest)