def name(name ="sk",age =23):
    print(name,age)

name("ponshivavel",23)

def name(**info):
    print(info,"hai")

name(name="ponshivavel",age=23)

def set(*info):
    print(sum(info))
    print(max(info))

set(1,2,3,4,5)

#lambda funtion
sq = lambda n: n*n
print(sq(4))

# recursion
def fun(n):
    if n>5:
        return 
    print(n)
    fun(n+1)

fun(1)
