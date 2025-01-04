import numpy as np

def sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
def sumradq(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+np.sqrt(i)
    return sum
def sumprod(n):
    sum=0
    prod=1
    for i in range(1,n+1):
        sum=sum+i
        prod=prod*i
    return sum, prod
def sumalfa(n,alfa=1):
    sum=0
    for i in range(1,n+1):
        sum=sum+i**alfa
    return sum
