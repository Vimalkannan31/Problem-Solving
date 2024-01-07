#Digit Count Program using python
def digit_count(n):
    res=0
    while n!=0:
        res+=1
        n=n//10  
    print("The Digit count:",res)

n=int(input("Enter the Number:"))     
digit_count(n)
        