def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here


    def trial():
        bucket = ['r','r','r','g','g','g']
        picked = []
        for i in range(3):
            randIndex = random.randint(0, len(bucket)-1)
            picked.append(bucket[randIndex])
            del bucket[randIndex]
        if picked[0] == picked[1] and picked[1] == picked[2]:
            return 1
        else:
            return 0
    homo = 0
    for i in range(numTrials):
        homo += trial()
    return homo/float(numTrials)

import random
import numpy

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if(x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))

def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = numpy.std(estimates)
    curEst = sum(estimates)/len(estimates)
    print 'Est. = '+ str(curEst) +\
        ', std. dev. = ' + str(round(sDev, 6))\
        + ', Needles = ' + str(numNeedles)
    return (curEst, sDev)

def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2.0:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst
