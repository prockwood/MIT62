import pylab

def openAndParse(file):
    hiTemps = []
    loTemps = []
    inFile = open(file)
    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            next
        else:
            hiTemps.append(int(fields[1]))
            loTemps.append(int(fields[2]))
    # print (hiTemps, loTemps)
    return (hiTemps, loTemps)

def producePlot(lowTemps, highTemps):
    diffTemps = []
    for i in range(len(lowTemps)):
        diff = highTemps[i] - lowTemps[i]
        diffTemps.append(diff)
    pylab.plot(range(1,32), diffTemps)
    pylab.title('Temp. Range in Boston for Each Day in July 2012 ')
    pylab.xlabel('Day')
    pylab.ylabel('Temperature Range')
    pylab.show()

def main():
    temps = openAndParse('julyTemps.txt')
    producePlot(temps[0], temps[1])

if __name__ == '__main__':
    main()
