#print 1 to 9 using "while Loop"
y = 1
while y<10:
    print(y, end=" ")
    y+=1
print()


#print ** ** ** using "while Loop"
x = 1
while x<4:
    print("**", end=" ")
    x=x+1
print()

#print ** * ** using "while loop"
a = 1
while a<4:
    if a%2 == 0 :
        print ("*", end=" ")
    else:
        print("**", end=" ")
    a=a+1
print()


#print 1 2 2 3 3 3 4 4 4 4
for i in range(1, 5, 1):
    for j in range(1, i+1, 1):
        print(i, end = " ")
print()


#print 1 1 3 1 3 5 1 3 5 7
for i in range(1, 8, 2):
    for j in range(1, i+1, 2):
        print(j, end = " ")