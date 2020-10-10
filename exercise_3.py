
"""
Write a function calculation() such that it can accept two variables and
calculate the addition and subtraction of it.
And also it must return both addition and subtraction in a single return call
"""
def calculation(a,b):
    return a+b,a-b

result=calculation(40,10)
print(result)
result=calculation(40000,5950)
print(result)
result=calculation(800,700)
print(result)
result=calculation(490,300)
print(result)
result=calculation(100,60)
print(result)

