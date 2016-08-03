import pylab

principal = 60000
interestRate = 0.15
years = 20
values = []

for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate


# pylab.plot(range(years+1), values)
# pylab.plot(range(years+1), values, 'r')
# pylab.plot(range(years+1), values, 'ro')
pylab.plot(values, linewidth = 30)



pylab.title('10% growth, Compounding anually', fontsize = 6)
pylab.xlabel("Years")
pylab.ylabel('Value of Principal ($)')
pylab.show()

"""
.rc file to change defaults of plot parameters

"""
