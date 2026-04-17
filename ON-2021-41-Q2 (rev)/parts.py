class Picture:
    def __init__(self, Heightp, Widthp, Decriptionp, Colourp):
        self.__Height=int(Heightp) #Integer
        self.__Width=int(Widthp) #Integer
        self.__Description=Decriptionp #string
        self.__Colour=Colourp

def GetDescription(self):
    return self.__Description
def GetColour(self):
    return self.__Colour
def GetHeight(self):
    return self.__Height
def GetWidth(self):
    return self.__Width

def SetDescription(self, descriptionp):
    self.__Description=descriptionp

PictureArray=[]
for i in range(100):
    PictureArray.append(Picture("",0,0,""))

def ReadData():
    Filename="Pictures.txt"
    Counter=0
    try:
        File=open(Filename,"r")
        Description=(File.readline()).strip().lower()
        if Description!="":
            Width=int(File.readline().strip())
            Height=int(File.readline().strip())
            Colour=File.readline().strip().lower()
            PictureArray[Counter]=Picture(Description, Width, Height, Colour)
            Description=(File.readline()).strip().lower()
            Counter=Counter+1
            File.close()
    except FileNotFoundError:
        print("Could not find file")
    return Counter, PictureArray


#main program
NumberofPictures, PictureArray=ReadData

Width=int(input("Enter the width of the picture"))
Colour=input("Enter the colour of the picture").lower
Height=int(input("Enter the Height of the picture"))

print("Matches Frame Shown")
for i in range(0, NumberofPictures):
    if PictureArray[i].GetColour()==Colour:
        if PictureArray[i].GetHeight()<=Height:
            if PictureArray[i].GetWidth()<=Width:
                print(PictureArray[i].GetDescription, "", str(PictureArray[i].GetHeight()), str( PictureArray[i].GetWidth()))













        