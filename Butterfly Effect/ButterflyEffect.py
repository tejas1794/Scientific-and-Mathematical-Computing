import math
from pylab import *
import numpy as np

def mayfly(x,b,t):
    '''Calculate Mayfly Population trajectories for two initial populations differing but 1e-5'''
    arrayx = []
    x2 = x + 1e-5
    arrayx2 = []
    #s = abs(x2-x) #initializing s
    #s0 = abs(x2-x) #Getting s at 0
    for i in xrange(t):
        #print x
        #subplot(211) #I tried creating subplots for analysis but putting them on the same graph gave a better idea
        #semilogy(i,s,'b.') #plot separation
        x = b*(1-x)*x
        arrayx.append(x)
        x2 = b*(1-x2)*x2
        arrayx2.append(x2)
        #s = abs(x2-x) #updating s
    #print "Final x is:"
    #print mean(arrayx), mean(arrayx2)
    #plot(arrayx,arrayx2, 'r.')
    return arrayx, arrayx2

def lls(x,b,t):
    '''Returns Least Linear Squares curve and respective growth rate'''
    x1,x2 = mayfly(x,b,t)
    #print x1,x2
    beta = (mean(np.multiply(x1,x2)) - (mean(x1)*mean(x2)))/(mean(np.multiply(x1,x1)) - mean(x1)**2)
    alpha = mean(x2) - (mean(x1)*beta)
    y = x + 1e-5
    for i in range(t):
        #subplot(212)
        semilogy(i, exp(alpha + (beta*i))/1e10,'r.')
        semilogy(i, abs(x2[i]-x1[i]),'k.')
        xlabel("Time (in years)")
        ylabel("Population")
    print alpha, beta

lls(0.5,3.9,50)
lls(0.1,4,15)