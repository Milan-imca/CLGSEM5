'''
    9. Create a tuple of list of 10 citites. Ask user to enter a city name and check if that city exists in the tuple or not. Also display how many times that city is there in tuple
'''


cities = ("Bangalore,Dubai,Ahmedabad,Mumbai,Kolkata,Surat,Jamanagar,Dubai,Delhi,Kashmir")

print(cities)

cityname = input("Enter city name : ")
if cityname in cities:
    countOfCity = cities.count(cityname)
    print(f"{cityname} is present {countOfCity} times in cities tuple")
else:
    print("city not present!")