# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 21:38:57 2018

@author: wang1
"""
import numpy as np
import math

def isPrime(m):
    if m % 2 == 0 and m > 2: 
        return False
    return all(m % i for i in range(3, int(math.sqrt(m)) + 1, 2))

def is_n_minus_k_divisible_by_m(n, k, m):
    if ((n-k) % m) == 0:
        return True
    else:
        return False

n = np.random.randint(0,1000)
print(n)
phrase = input('Do you want to ask, guess or quit :' )
g = -1
t = 0
score = 0
while not phrase == "quit": 
    
    if phrase == "ask":
        t += 1
        print ('If we subtract k from n, is the result divisible by m? ' )
        k = int(input('Type value of k : '))
        m = int(input('Type value of m : '))
        if not (isPrime(m)): raise Exception("m must be a prime")
        if (k < 0) or (k>=m) or (m>=1000) : raise Exception("we only except 0 <= k< m < 1000")           
        if is_n_minus_k_divisible_by_m(n, k, m):
            print('disvisble')
        else:
            print('not disvisble')
        t += 1
        
    if phrase == "guess" :
        t += 1
        g = int(input('please guess a number : '))        
        if g == n :
            print ('Congraulation! Correct!')
            break
        else:
            print('Wrong!')
    phrase = input('Do you want to ask, guess or quit :' )
   
if phrase == "quit" :
    print('your score is 0 !')
else :
    score = int(n / t)
    print(score)
    print('your score is : ' + str(score))
    
   
