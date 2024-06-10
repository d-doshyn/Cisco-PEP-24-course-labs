def liters_100km_to_miles_gallon(liters):
    liters_km = liters / 100
    km_liters = 1 / liters_km
    mile_liters = km_liters / 1.609344
    mile_gallon = mile_liters * 3.785411784
    return mile_gallon

def miles_gallon_to_liters_100km(miles):
    gallon_miles = 1 / miles
    gallon_km = gallon_miles / 1.609344
    liters_km = gallon_km * 3.785411784
    liters_100km = liters_km * 100
    return liters_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))