#!/usr/bin/python
mph_input = raw_input("Please enter a speed in miles/hour: ")

if mph_input.isalpha():
    print "Miles/hour should be entered as a number, not anything else!"
    exit()

mph = int(mph_input)

yards_per_mile = 1760
meters_per_hour = mph * 1609.34
feet_per_hour = mph * 5280

meters_per_day = meters_per_hour * 24
barleycorns_per_day = meters_per_day * 117.647

yards_per_hour = 1760 * mph
furlongs_per_hour = yards_per_hour = yards_per_hour / 220
furlongs_per_day = furlongs_per_hour * 24
furlongs_per_week = furlongs_per_day * 7

mach = (feet_per_hour / 60 / 60) / 1130

psl = ((meters_per_hour / 60 / 60) / 299792458) * 100

print "Original speed in miles/hour is %.2f" % (mph)
print "Converted to barleycorn/day is: %.2f" % (barleycorns_per_day)
print "Converted to furlongs/fortnight is: %.2f" % (furlongs_per_week * 2)
print "Converted to Mach number is %f:" % (mach)
print "Converted to the percentage of the speed of light is: ", psl