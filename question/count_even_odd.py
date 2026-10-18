list = [10, 22, 15, 7, 8, 13 ]


even = 0
odd = 0

for i in list:
    if i%2 == 0:
        even = even+1

    elif i%2 !=0:
        odd+=1

print("even", even)
print("odd", odd)