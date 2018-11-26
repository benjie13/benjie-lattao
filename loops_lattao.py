print ("2 to 10")
for x in range (2,12,2):
    print(x)

print ("3 to 15")
for y in range(3,18,3):
        print(y)

print ("4 to 20")
for z in range (4,24,4):
        print(z)

print ("12 to 36")
for a in range (12,48,12):
        print(a)

#nested loop sample
print ("Multiplication")
for y in range (1,11):
    for z in range (1,11):
        print(z * y, end='\t')
    print()

print ("Multiplication 10 - 20")
for y in range (10,21):
    for z in range (1,11):
        print(z * y, end='\t')
    print()
