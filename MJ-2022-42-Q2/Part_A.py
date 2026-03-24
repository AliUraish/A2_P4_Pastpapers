import random
arraydata=[[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        arraydata[i][j]=random.randint(0,100)

#part b
arraylength=10
for x in range(0, arraylength):
    for y in range(0, arraylength-1):
        for z in range(0, arraylength - y - 1):
            if arraydata[x][z] > arraydata[x][z+1]:
                tempnumber=arraydata[x][z]
                arraydata[x][z]=arraydata[x][z+1]
                arraydata[x][z+1]=tempnumber

#part c
def printarray(arraydata):
    for i in range(10):
        for j in range(10):
            print(arraydata[i][j], end=" ")
        print()

arraydata=[[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        arraydata[i][j]=random.randint(0,100)

print("Before sorting:")
printarray(arraydata)

arraylength=10
for x in range(0, arraylength):
    for y in range(0, arraylength-1):
        for z in range(0, arraylength - y - 1):
            if arraydata[x][z] > arraydata[x][z+1]:
                tempnumber=arraydata[x][z]
                arraydata[x][z]=arraydata[x][z+1]
                arraydata[x][z+1]=tempnumber

print("After sorting:")
printarray(arraydata)