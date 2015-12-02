import math
from pylab import *
from decimal import *
import numpy as numpy

def maxFloatingPoint():
    '''Returns Max Floating Point number'''
    start = 1.0
    while not math.isinf(start):
        res = start
        start = start*1.1
    print res

def minFloatingPoint():
    '''Returns Min Floating Point number'''
    start = 1.0
    res= 2.0*start
    while res > start > 0:
        res = start
        start = start*0.5
    return res

def machineEpsilon(func=float): #it accepts float, float-64 and float-32
    '''Returns Machine Epsilon'''
    ep = func(1)
    while not (func(1)+func(ep) == func(1)):
        res = ep
        ep = func(ep) / func(2)
    return res

def bitCounter():
    '''Returns Mantissa and Exponent bits'''
    counterArray = str(Decimal(math.sqrt(2)))
    print (Decimal(math.sqrt(2))), math.sqrt(2)
    print 'Mantissa: ', len(counterArray[2:])
    print 'Exponent (64-Mantissa-SignBit): ', 63-len(counterArray[2:])
    res = [1,63-len(counterArray[2:]),len(counterArray[2:])]
    return res

def biasCalculation():
    '''Returns min and max biases'''
    min = ((2**11)-1)/2 - 1
    max = ((2**11)-1)/2 + 1
    print 'Min Exp is: ', min, 'Max Exp is: ', max
    return min,max

maxFloatingPoint()
minFloatingPoint()
machineEpsilon(float)
machineEpsilon(numpy.float64)
machineEpsilon(numpy.float32)
bitCounter()
biasCalculation()
print numpy.finfo(numpy.float) #Our base for getting actual values.