def Factorial(n):
    if n<2:
        return 1
    else:
      return  n * Factorial(n-1)

n=int(input("Enter a number: "))
r=Factorial(n)
print(f"Factorial of {n} is: ",r)