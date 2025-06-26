
print("Enter Your Number:")
User_Input= int(input())

def Factorial (User_Input):
  if User_Input < 2:
    return 1
  else:
    return User_Input * Factorial(User_Input-1)

Total = Factorial(User_Input)
print("The factorial is:",Total)




