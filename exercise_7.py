"""
Assign a different name to function and
 call it through the new name
 """
def studentname(name,age):
    print(name,age)

student = studentname
student("Rushi",16)
student("Shyam",16)
student("Sandeep",17)
student("Pradeep",15)