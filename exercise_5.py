"""
 Create an inner function
 to calculate the addition in the following way

Create an outer function that will accept
 two parameters a and b
Create an inner function inside an
 outer function that will calculate the addition of a and b
At last, an outer function will
 add 5 into addition and return it
"""
def outerfunction(a,b):
    square  = a**2
    def innerfunction(a,b):
        return a+b
    add = innerfunction(a,b)
    return add+5

result = outerfunction(10,3)
print(f" The result is result " + str(result))