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