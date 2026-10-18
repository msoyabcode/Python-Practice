list = [10, 22, 15, 7, 2, 2, 5, 5,  8, 13 ]


dubplicate = []

for i in list:

    if list.count(i)>1 and i not in dubplicate:
        dubplicate.append(i)


print(dubplicate)