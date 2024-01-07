#Prime number checking using python
def prime_check(n):
    flag=0
    for i in range(2,n):
        x=n%i
        if x==0:
            flag+=1
            break
    if flag==1:
        print(n,"is a Not prime number")
    else:
        print(n,"is a prime number")


n=int(input("Enter the Number:"))    
prime_check(n)
    