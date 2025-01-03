def liters_100km_to_miles_gallon(liters):
    kilometers_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    
    miles_per_gallon = (100 / kilometers_per_mile) / (liters / liters_per_gallon)
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    kilometers_per_mile = 1.609344
    liters_per_gallon = 3.785411784
    
    liters_per_100km = (100 / (miles * kilometers_per_mile)) * liters_per_gallon
    return liters_per_100km

# Test cases
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))