"""
Create a function showEmployee() in such a way that it should accept employee name,
 and it’s salary and display both,
 and if the salary is missing in function call it should show it as 10000
"""
def showEmployee(name, salary=10000):
    print("Employee name is", name, "and his salary is", salary)

showEmployee("Shyam",10000)
showEmployee("Sandeep",8000)
showEmployee("Phani",12000)
showEmployee("Pradeep",9500)
