#PYTHON
#--------------------------print("ABOUT THE STRING")-----------------------------

n = input("ENTER THE STRING : ")

print(n)
s1 = "Python"
s2 = 'Programming'
s3 = """This is
a multi-line
string"""
text = n

print(n[0])     #R    INDEX
print(n[1])     #O
print(n[-1])    #INDEX FROM LAST
print(n[0:4])   # Prog

print(len(n))   #length
print("Hi " * 3)  #String Repetition
print(n.upper())   #upper case
print(n.lower())   #lower case

#----------------------String modifies----------
print(text.capitalize()) #cap the first letter
print(text.replace("java", "Python"))
print(text.find("python"))
print(text.count("a"))

#----------------------string check----------------
print(text.split())
print(text.isalpha())    # False
print(text.isdigit())    # False
print(text.isalnum())    # True
print(text.startswith("Py"))   # True
print(text.endswith("123"))    # True
name ="sK"
age =21
print(f"My name is {name} and I am {age} years old.")

#---------------------charAT------------------

for ch in text:
    print(ch)


#---------------------reverse------------------
    
print(text[::-1])
