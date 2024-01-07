#sum the number till the one digit of the number using python
def digit_count(n):
    count=0
    while n!=0:
        x=n%10
        count+=1
        n//=10
    return count

n=int(input("Enter the number:"))
sum=0 
k=digit_count(n)
while k!=1:
    while n!=0:
        y=n%10
        sum+=y
        n//=10
    k=digit_count(sum)
    n=sum
    sum=0
    
print("sum the number till the one digit is:",n)