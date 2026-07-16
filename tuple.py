tuple=(1,2,3,4,5,6,7,2)
print(tuple[-1],"    ",tuple[0])
n =len(tuple)//2
print(tuple[n-1:n+2])
for i in tuple:
     if 1<tuple.count(i):
          print(i)
print(tuple.index(5))