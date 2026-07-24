student ={"name":"ponshivavel","Age" : 21,"city":"erode"}
print(student["name"])
student["Age"]=22
student["course"]="AI & DS"
print(student.keys)
print(student.values)
for key , value in  student.items():
    print(key,"  ",value)
print(student.pop("city"))
student.clear()
print(student)
