a = int(input("enter the number"))
n =a
sum =0
while n>0:
    d = n%10
    sum =sum*10+d
    n//=10
if a==sum:
    print("same")
else :
    print("sorry not same")