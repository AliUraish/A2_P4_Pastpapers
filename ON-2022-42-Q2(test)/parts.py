class Character:
    #PRIVATE NAME
    #PRIVATE XCOORDINATE
    #PRIVATE YCOORDINATE
    def __init__(self, Namep, XCoordinatep, YCoordinatep):
        self.__Name=Namep
        self.__XCoordinate=XCoordinatep
        self.__YCoordinate=YCoordinatep
    def GetName(self):
        return self.__Name
    def GetXCoordinate(self):
        return self.__XCoordinate
    def GetYCoordinate(self):
        return self.__YCoordinate
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate=self.__XCoordinate+XChange
        self.__YCoordinate=self.__YCoordinate+YChange

#main program
Characters=[]
filetext="Characters.txt"
try:
    file=open(filetext, "r")
    for i in range(0,10):
        Name=file.readline().strip()
        XCoord=file.readline().strip()
        YCoord=file.readline().strip()
        SaveChar=Character(Name, int(XCoord), int(YCoord))
        Characters.append(SaveChar)
    file.close()
except:
    print("File not found")


Position=-1
CharacterInput=input("Enter the name of the character").lower()
for i in range(0, 10):
    Charactername=str(Characters[i].GetName()).lower()
    if CharacterInput==Charactername:
        Position=i

valid=False
while valid!=True:
    Move=input("Enter a letter to move")
    if Move.upper()=="A":
        Characters[Position].ChangePosition(-1,0)
        valid=True
    elif Move.upper()=="W":
        Characters[Position].ChangePosition(0,1)
        valid=True
    elif Move.upper()=="S":
        Characters[Position].ChangePosition(0,-1)
        valid=True
    elif Move.upper()=="D":
        Characters[Position].ChangePosition(1,0)
        valid=True

print(
    Charactername,
    "has changed to coordinate X=" + str(Characters[Position].GetXCoordinate())
    + " Y=" + str(Characters[Position].GetYCoordinate()),
)
