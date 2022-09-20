# 9. Write a Python script to create a list of city names taken from the user.

total_cities=int(input("Enter how many city name you want to enter "))
l=[]
for i in range(total_cities):
    city=input(" Enter city name ")
    l.append(city)
print(l)