import math
from pylab import *

def plottingData(inputFile,rowsToSkip):
    '''returns plot of certain columns in the given data file after skipping a number of rows.'''
    data = loadtxt(inputFile,skiprows = rowsToSkip)
    mins = data[:,0]
    print "Minutes: ",mins
    secs = data[:,1]
    print "Seconds: ",secs
    temp = data[:,5]
    print "Temperature: ",temp
    time = mins + secs/60.
    print "Time: ",time
    plot(time,temp)
    ylim(-30.1,27.5)
    xlabel("Time (in min.)")
    ylabel("Temperature (in C)")
    title("Effect of Altitude on Balloon flight")

plottingData("balloon.dat",138)