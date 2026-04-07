DataArray=[]

try:
    DataFile=open("Data.txt", "r")
    for line in DataFile:
        DataArray.append(int(line))
        DataFile.close()
except FileNotFoundError:
    print("File not Found")

def printarray(DataArray):
    output=""
    for i in range(0, len(DataArray)):
        output=output+str(DataArray[i])+" "
    print(output)

printarray(DataArray)


def linear_search(DataArray, value):
    count=0
    for i in range(0, len(DataArray)):
        if DataArray[i]==value:
            count=count+1
    return count


inputvalue=int(input("Enter a value to search for between 0 and 100: "))
while inputvalue<0 or inputvalue>100:
    print("invalid input")
    inputvalue=int(input("Enter a value to search for between 0 and 100: "))

Number_times=linear_search(DataArray, inputvalue)
print("The number,",inputvalue,"is found",Number_times,"times")
