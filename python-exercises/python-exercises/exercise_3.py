#!/usr/bin/python
mph_input = raw_input("Please enter a speed in miles/hour: ")

if mph_input.isalpha():
    print "Miles/hour should be entered as a number, not anything else!"
    exit()

mph = int(mph_input)

yards_per_mile = 1760
meters_per_hour = mph * 1609.34
feet_per_hour = mph * 5280


print "Original speed in miles/hour is %.2f" % (mph)
print "Converted to barleycorn/day is: %.2f" % (barleycorns_per_day)
print "Converted to furlongs/fortnight is: %.2f" % (furlongs_per_week * 2)
print "Converted to Mach number is:" % (mach)
print "Converted to the percentage of the speed of light is: ", psl