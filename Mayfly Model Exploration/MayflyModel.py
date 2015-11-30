import math
from pylab import *

def fixedb(x,b,t):
    '''Provides the relationship between a specific growth rate b and population x over time t. '''
    for i in xrange(t):
        #print x
        plot(i,x,'b.')
        x = b*(1-x)*x
    #print "Final x is:"
    return x

def rangedb(x,b,tmin,tmax):
    '''Returns a relationship between multiple values of b, x over a certain time period'''
    b = linspace(0, b, 401) #Giving us increment of 0.01 per b
    for i in xrange(tmax):
        if i > tmin:
            plot(b, x, 'b.',alpha = 0.5, ms = 0.3)
            xlabel('Growth Rate')
            ylabel('Population')
            title('Population vs Growth Rate of Mayflies')
            xlim(0.0,4.0)
            ylim(0.0,1.0)
        x = b*(1 - x)*x
    #for i in range(0,len(b),10): #This code gives the growth rate vs population final result.
    #    print "At Growth Rate: ", b[i], "-> Population after 100 years is: ", x[i]
    return x
    
fixedb(0.1,0.0,100)
fixedb(0.1,1.11,100)
fixedb(0.1,2.51,100)
fixedb(0.1,3.41,100)
fixedb(0.1,4.0,100)
rangedb(0.1,4.0,0,100)