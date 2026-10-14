num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

for i in range(num1, num2+1):
    for j in range(2, i):
        if i%j==0:
           break
    else:
        if i>1:
         print(i)
    