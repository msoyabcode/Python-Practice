# num = int(input("Enter number: "))

# isPrime = True

# if num<=1:
#     isPrime = False

# else:
#     for i in range(2, num, ):
         
#         if num%i==0:

#            isPrime = False
#            break

# if isPrime:
#     print("prime") 
# else:
#     print("not primee")    


num = int(input("Enter number: "))

if num<=1:
    print("not prime")

else:
    for i in range(2, num):
        if num%i == 0:
            print("not prime")
            break
    else:
        print("prime")


# Naya concept: Python mein for loop ka else tab execute hota hai jab loop break ke bina complete ho jaata hai.

# Divisor mil gaya → break → Not prime

# Koi divisor nahi mila → loop complete → Prime