"""
Write a 
recursive function to calculate the sum of numbers from 0 to 10
"""

def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(f"The result is " + str(res))

res = calculateSum(20)
print(f"The result is " + str(res))

res = calculateSum(30)
print(f"The result is " + str(res))