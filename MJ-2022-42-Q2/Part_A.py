import random
arraydata=[[0]*10 for i in range(10)]
for i in range(10):
    for j in range(10):
        arraydata[i][j]=random.randint(0,100)