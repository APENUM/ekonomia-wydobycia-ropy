# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 18:50:56 2016

@author: szymon
"""
from scipy.optimize import newton
import numpy as np

q=np.array([11.952,10.304,9.005,8.029,7.217,6.565,6.015,5.546,5.177])
Gp=np.array([0,2.005,3.819,5.355,6.78,8.039,9.2,10.276,11.184])
t=np.arange(0,4.5,0.5)*365
qi=q[0]; q2=q[-1]; t2=t[-1]; q1=np.sqrt(qi*q2); t1=1.68*365;

def func(b):
    return t2*(qi/q1)**b - t1*(qi/q2)**b - (t2-t1)
def fprime(b):
    return t2*(qi/q1)**b * np.log(qi/q1) - t1*(qi/q2)**b * np.log(qi/q2)
b=newton(func,1,fprime)
Di=((qi/q2)**b-1)/(b*t2)
t=np.arange(0,30)*365
#nowe wartośći:
q=qi/(1+b*Di*t)**(1/b)
Gp=(qi/(Di*(1-b)))*(1-(q/qi)**(1-b)) / 1E3

#print Gp

