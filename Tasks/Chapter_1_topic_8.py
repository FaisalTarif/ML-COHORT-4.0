#Task 1
print("Task 1")
x = input("Enter 1st Number: x = ")
y = input("Enter 2nd Number: y = ")
z = input("Enter 3rd Number: z = ")

if x>y and x>z:
    print("x is largest")

elif y>x and y>z:
    print("y is largest")

else:
    print("z is largest")



#Task 2
print("Task 2")
p = input("Enter CGPA of Person 1 : ")
q = input("Enter CGPA of Person 2 : ")
r = input("Enter CGPA of person 3 : ")

if p<q and p<r:
    print("Person 1 has the lowest CGPA")

elif q<p and q<r:
    print("Person 2 has the lowest CGPA")

else:
    print("Person 3 has the lowest CGPA")

p = float(p)
q = float(q)
r = float(r)

d = (p+q+r) / 3

print( "The average CGPA is ", d)