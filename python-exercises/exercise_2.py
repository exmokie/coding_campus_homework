#!/usr/bin/python
gallons = raw_input("Please enter the number of gallons: ")
gallons = float(gallons)
liters = gallons * 3.7854
barrels_oil = (float(42)/19.5) * gallons
pounds_co2 = gallons * 20
ethanol_gallons = (gallons * float(115000)) / float(75700)
dollars = gallons * float(4)

print "%.2f gallons is the equivalent of %.2f liters" % (gallons,liters)
print "%.2f gallons of gasoline requires %.2f barrels of oil " % (gallons,barrels_oil)
print "%.2f gallons of gasoline produces %.2f pounds of CO2 " % (gallons,pounds_co2)
print "%.2f gallons of gasoline is energy equivalent to %.2f gallons of ethanol" % (gallons,ethanol_gallons)
print "%.2f gallons of gasoline requires %.2f US dollars" % (gallons,dollars)