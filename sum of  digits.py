#sum of digits using python
def sum_of_digit(n): 
    res=0
    while n!=0:
        x=n%10
        res+=x
        n//=10
    print(res)
n=int(input("Enter the Number:"))    
sum_of_digit(n)