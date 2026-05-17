def ReadData():
    colour=input("Enter a colour filename: ")
    Array=[]
    try:
        file=open(colour)
        for line in file:
            Array.append(line.strip())
        file.close()
    except FileNotFoundError:
        print("File not found")
    return Array

def Spltdata(DataArray):
    red=[]
    green=[]
    blue=[]
    orange=[]
    yellow=[]
    pink=[]
    for i in range(0, len(DataArray)):
        split=Line.split(",")

        if split[1].strip()=="red":
            red.append(split[0].strip())
        elif split[1].strip()=="green":
            green.append(split[0].strip())
        elif split[1].strip()=="blue":
            blue.append(split[0].strip())
        elif split[1].strip()=="orange":
            orange.append(split[0].strip())
        elif split[1].strip()=="yellow":
            yellow.append(split[0].strip())
        elif split[1].strip()=="pink":
            pink.append(split[0].strip())
StoreData(red, "Red.txt")
Storedata(green, "Green.txt")
StoreData(blue, "Blue.txt")
StoreData(orange,"Orange.txt")
StoreData(yellow, "Yellow.txt")
StoreData(pink, "Pink.txt")



def StoreData(DataToStore, filename):
    try:
        file=open(filename,"w")
        for i in range(0, len(DataToStore)):
            file.write(Item)
            file.write("\n")
        file.close()
    except:
        print("Error in opening file")
                        

#main program
DataofFile=ReadData()
SplitData(DataofFile)
