import math

#part a
#iterated logarithm
def logStar(n):
    if n <= 1:
        return 0
    else:
        return 1 + logStar(math.log(n))

n = 10**12
print(logStar(n))

""" 
n1 = 2
def f_star(n):
    if n <= 1:
        return 0
    else:
        return 1 + f_star(n/2)

result = f_star(n)
print(result)
 """

#part b