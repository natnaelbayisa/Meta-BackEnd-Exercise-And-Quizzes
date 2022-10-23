import calendar

#leap days or years means that divisible by 4
leapdays = calendar.leapdays(2000,2050) # tell us leapdays b.n 2000 & 2050
print(leapdays)

isitleap = calendar.isleap(2000) #return boolean value
print(isitleap)