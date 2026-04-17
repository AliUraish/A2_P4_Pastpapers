class Balloon:
    def __init__(self, DefenceItemp, Colourp):
        self.__DefenceItem=DefenceItemp
        self.__Colour=Colourp
        self.__Health=100
    def GetDefenceItem(self):
        return self.__DefenceItem
    def ChangeHealth(self, change):
        self.__Health=self.__Health+change
    def CheckHealth(self):
        if self.__Health==0 or self.__Health<0:
            return True
        else:
            return False
    


def Defend(balloon):
    strength=int(input("Enter the strength"))
    balloon.ChangeHealth(-strength)
    print("you defended with", str(balloon.GetDefenceItem()))
    if balloon.CheckHealth()==True:
        print("your defence was unsuccessful")
    else:
        print("Your defence was successful")
    return balloon


#main program
defence=input("input a defence item")
colour=input("input a colour")
Balloon1=Balloon(defence, colour)
Balloon1=Defend(Balloon1)


