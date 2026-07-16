a = int(input("enter the number"));
b = int(input("enter the number"));
lcm = max(a,b)
while True :
   if lcm %a==0 and lcm %b==0:
      print(lcm)
      break
   lcm+=1