set = {1,1,2,3,4,5,6,7,7}
set2 ={9,8,7,6,6}
print(set)
set.add(3)
print(set)

set.remove(4)
print(set)

set.discard(2)
set.intersection(set,set2)
set.union(set,set2)
set.symmetric_difference(set2)

print(set.pop())
for i in range(len(set)):
    print(i)

