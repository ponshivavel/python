# for i in range(5):
#     for j in range(5-i):
#         print("* ",end="")
#     print()

#output
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# for i in range(5):
#         print("* ",end="")
#     print()

# output
    
# * 
# * * 
# * * * 
# * * * * 
k =64

for i in range(5):
    for j in range(i):
       print(chr(k+j+1),end="")
       
    print()
