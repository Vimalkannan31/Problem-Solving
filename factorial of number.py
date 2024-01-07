#Factorial of the given number using python
def factoril_num(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Factorial of given number is:",fact)
    
n=int(input("Enter the number:"))
factoril_num(n)