DataArray=[0 for i in range(100)]

def ReadFile():
    global DataArray
    try:
        DataFile=open("Integer.txt", "r")
        for line in DataFile:
            DataArray.append(int(line))
        DataFile.close()
    except FileNotFoundError:
        print("File not found")

def FindValue():
    global DataArray
    inputvalue=int(input("Enter a value to search"))
    while inputvalue<0 or inputvalue>100:
        print("invalid input")
        inputvalue=int(input("Enter a value to search between 0 and 100: "))
    Number_times=0
    for i in range(0, len(DataArray)):
        if DataArray[i]==inputvalue:
            Number_times+=1
    return Number_times

ReadFile()
print("The number appears",FindValue(),"times")

