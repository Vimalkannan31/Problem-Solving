#convert binary to decimal using python program
def binary_to_decimal(n):
    sum=0
    x=1
    while n!=0:
        y=n%10
        sum+=y*x
        x*=2
        n//=10
    print(sum)
    
n=int(input("Enter the number:"))
binary_to_decimal(n)