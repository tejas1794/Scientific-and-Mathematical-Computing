import math
from pylab import *
def isPerfectSquare(a,b):
    """Returns 1 if result of ((input1)^2 + (input2)^2) is a perfect square"""
    cSq = (a*a) + (b*b);
    c = math.sqrt(cSq);
    if(c == math.floor(c)): return 1;
    else: return 0;

def myGCD(a,b):
    """Returns GCD of 2 numbers"""
    while(a!=b):
        if(a>b): a=a-b;
        else: temp = a; a = b; b = temp;
    return a;

def isPrime(a):
    """Returns 1 if a number is prime, 0 if not"""
    count = 0;
    if a>=1:
        for i in xrange(1,a+1):
            #print a%i;
            if((a%i) == 0): count += 1;
        #print 'count = ' + str(count) ;
        if(count <= 2): return 1;
        else: return 0;

def ppt(a):
    '''Returns set of Primitive Pythagorean Triplets upto the input'''
    print'Generating Primitive Pythagorean Triplets...'
    ichart = []
    jchart = []
    for i in xrange(1,a+1):
        for j in xrange(1,a+1):
            #if(myGCD(i,j)==1): #CASE 1- All pythagorean triples
            if(myGCD(i,j)==1 and j%2==0): #Case 2 - Primitive Pythagorean Triples
            #if(myGCD(i,j)==1 and i<j and isPrime(i)): #Case: Further Analysis: Prime only triples
                if(isPerfectSquare(i,j)==1): 
                    #print i, j, int(math.sqrt((i*i)+(j*j))) #Get the list of triples
                    ichart.append(i)
                    jchart.append(j)
    print 'Completed generating triplets.'
    total = len(ichart)
    plot(ichart,jchart,'b.')
    xlabel('a')
    ylabel('b')
    title("Primitive Pythagorean Triples")
    show()
    return total #Total number of triplets generated

ppt(5000) #Check PPTs in first 5000 int


        
        