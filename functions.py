def printsk():
  return("sk")

def add(a,b):
  print(a+b)
def large(a,b):
 print(check(a,b))
 if a>b:
    return a
 else: return b

def check(a,b):
  if a%2==0:
    return "even"
  else:
    return "odd"
    
print(printsk())

print(add(12,24))  
print(large(12,22))

#if not return adn call the funtion there prient along withanwer is None

def sqr(a):
  return a*a
print(sqr(12))