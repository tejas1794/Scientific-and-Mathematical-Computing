import math
from pylab import *

def primeListGen(k):
    '''Generates a list of prime numbers up to number 'k' using the algorithm "Sundaram's Sieve" '''
    allK = range(3, k+1, 2)
    half = (k)//2
    init = 4
    for j in xrange(3, k+1, 2):
        for i in xrange(init, half, j):
            allK[i-1] = 0
        init += 2*(j+1)
        if init > half:
            return [2] + filter(None, allK)

def isPrime(a):
    '''Checks against the generated list of primes and determines if input 'a' is a prime number'''
    listOfPrimes = primeListGen(a+1)
    if a in listOfPrimes:
        return 1
    else: 
        return 0
    
def isCNumber(n):
    '''Checks if the given number 'n' fulfills the criterion for a C-Number'''
    for i in xrange(2,n):
        if (pow(i,n) % n == i):
            #print i, pow(i,n), pow(i,n) % n #Get the fulfilled C-Number equation
            continue
        else:
            return 0
    return 1

def cVsPrime(n):
    '''Returns all non-prime C-Numbers from in the interval (2,n)'''
    nonPrimeCNumbers = []
    for i in xrange(2,n):
        if(isCNumber(i)==1 and isPrime(i)!=1):
            nonPrimeCNumbers.append(i)
            #print "Found One!"
            #break
    print "All Done!"
    print nonPrimeCNumbers #Added this to show results outside of console
    return nonPrimeCNumbers

cVsPrime(2500)