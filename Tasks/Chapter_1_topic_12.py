#Task 1
num = [1, 3, 5, 7, 9]
num.append(10)
a = num[1]
num.remove(a)
print(num)

sum = 0
for i in range(0, 5, 1):
    sum = sum + num[i]

print("The sum of the elemets is: ", sum)
print()


#Task 2
city = ("Dhaka", "Rajshahi", "Chapainawabganj", "Naogaon", "Cox's Bazar")
print("The 3rd element of the touple is: ", city[2])

city = list(city)
city.append("Chittagong")

city = tuple(city)
print("The modified tuple is:", city)
print()

#Task 3
marks = {"Electronics": 88, "Measurement": 82, "Machine II": 51}

marks["HUM"] = 75
marks["Machine II"] = 55

print(marks)