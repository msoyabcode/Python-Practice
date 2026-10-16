num = int(input("Enter number: "))

original = num

finalNumber = original

count = 0

total = 0


while num > 0:
    lstDi = num % 10
    count = count+1

    num = num // 10

print(count)


while original>0:
    lastdigit = original % 10
    total = total+ lastdigit**count
    original = original // 10

if finalNumber == total:
    print("Armstrong")
else:
    print("not Armstrogn")