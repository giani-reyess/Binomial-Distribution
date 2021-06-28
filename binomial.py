import numpy as np
import math as m 
from fractions import Fraction

def binomial(n,x):
    formula = m.factorial(n) / (m.factorial(x) * m.factorial(n-x))
    return formula

def main(n,x,p):
    q = (1 - p)**(n-x)
    p **= x
    P = binomial(n,x) * p * q
    
    return round(P*100,2)

if __name__ == '__main__':
    
    n = int(input(print('Insert n:')))
    k = int(input(print('Insert k:')))
    prob = Fraction(input(print('Insert probability of x like n,n:')))
    print(type(prob))

    binomial(n,k)
    print(main(n,k,prob))

