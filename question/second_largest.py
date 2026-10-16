list = [34, 45, 34, 90, 80, 45 ,2 ]

second_lar = list[0]

largest = list[0]

for i in list:
    if i>largest:
        second_lar = largest
        largest = i
    elif i<largest and i>second_lar:
        second_lar = i  


print(second_lar)