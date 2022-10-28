# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 00:55:18 2022

@author: user
"""

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def function(x):
    res = -15*((math.sin(2*x))**2) - (x-2)**2 + 160
    return res   

vfun = np.vectorize(function) #vectorized function

#Plot the graph
x = np.linspace(-10,10,20000)
y = vfun(x)
plt.plot(x,y)

'''PSO Function'''
def PSO(start,end,function,iterations,no_of_particles, w = 1, c1=2 ,c2=2):
    
   #PSO Intialization
    x=[] #position
    v=[] #velocity
    pbest=[]
    gbest=start
    for j in range(no_of_particles):
         x.append(start + (end-start)*random.random())   
         v.append(random.random())                      
         pbest.append(start)
    
    
    #PSO Iterations
    for i in range(iterations):
        r1 = random.random()
        r2 = random.random() 
        
        for j in range(no_of_particles):
            if function(pbest[j])< function(x[j]):
                pbest[j]=x[j]
            if function(pbest[j])>function(gbest):
                gbest=pbest[j]
                
        for j in range(30):
            v[j]= w*v[j] + c1*r1*(pbest[j]-x[j]) + c2*r2*(gbest-x[j])
            x[j]= v[j]+ x[j]
            
            
    return gbest

gbest = PSO(-10,10,function,500,30) #Optimised value of x
print(f'The optimised value of x is {gbest} & corresponding function value is {function(gbest)}')