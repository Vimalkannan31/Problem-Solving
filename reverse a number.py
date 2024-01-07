#reverse a given number using python
def reverse_number(n):
    res=0
    while n!=0:
        x=n%10
        res=(res*10)+x
        n//=10
    print(res)
n=int(int(input("Enter the number:")))
reverse_number(n)