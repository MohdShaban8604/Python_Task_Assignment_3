def Factorial(n):
    if n==0:
        return 1
    else:
        return n*(Factorial(n-1))
num =int(input("Enter the number : "))
print("Factorial of",num,"is : ",Factorial(num))