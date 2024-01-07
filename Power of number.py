#Power of given number using python
def power_of_num(b,p):
    pow=1
    for i in range(0,p):
        pow*=b
    print(pow)

b=int(input("Enter the Base Number:"))
p=int(input("Enter the Power of Number:"))
power_of_num(b,p)