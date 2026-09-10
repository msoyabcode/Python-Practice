# Take three numbers and find the largest number.

# firstNum = int(input("Enter first number: "))
# secondNum = int(input("Enter second number: "))
# thirdNum = int(input("Enter third number: "))

# if firstNum>secondNum and firstNum>thirdNum:
#     print(f"largest num is fist numbe: {firstNum}")

# elif secondNum>firstNum and secondNum>thirdNum:
#      print(f"largest num is second numbe: {secondNum}")

# else:
#       print(f"largest num is third numbe: {thirdNum}")
     


# Create a simple login system.

# Example:

# Username: admin
# Password: 1234

# If both are correct:

# Login Successful

# Otherwise:

# Invalid Username or Password


username = "admin"
password = 1234

userinput = input("Enter user name: ")
inputPassword = int(input("Enter password: "))

if username == userinput and password == inputPassword:
    print("Login Successful")

else:
    print("Invalid username or password")