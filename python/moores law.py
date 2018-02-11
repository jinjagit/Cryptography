keysPerSec = 1E13
keysPerDay = keysPerSec * 60 * 24
keysToSearch = (2**128) / 2
daysPerSearch = keysToSearch / keysPerDay
years = 0.0

print()
print("Finding number of years until %s keys can be searched in one day or less" % (keysToSearch))

while (daysPerSearch > 1):
    keysPerDay = keysPerDay * 2
    daysPerSearch = keysToSearch / keysPerDay
    years = years + 1.5
    print ("In %s years the average search will take %s days" % (years, daysPerSearch))

print()
print("Years: %s" % (years))
