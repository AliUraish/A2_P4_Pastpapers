DataArray=[]

try:
    DataFile=open("Data.txt", "r")
    for line in DataFile:
        DataArray.append(int(line))
        DataFile.close()
except FileNotFoundError:
    print("File not Found")

