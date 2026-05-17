class Card:
    def __init__(self, Numberp, Colourp):
        self.__Number=Numberp
        self.__Colour=Colourp
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour


Card=[Card() for i in range(0,29)]
try:
File=open("CardValues.txt","r")
for i in range(0,29):
    Card[i]=Card(file.readline().strip(),file.readline().strip())
    file.close()
except FileNotFoundError:
    print("File not found")


def ChooseCard():
    global Card
    global NumbersChosen
    flag=True
    while flag==True:
        inputnumber=int(input("Enter a number between 1 and 29: "))
        if inputnumber<1 or inputnumber>30:
            print("Invalid number")
        elif NumbersChosen[inputnumber-1]==True:
            print("Number already chosen")
        else:
            print("Valid")
            flag=False
            NumbersChosen[inputnumber-1]=True
            return CardSelected-1

#main
NumbersChosen=[False for i in range(0,30)]
player1=[]
for x in range(0,4):
    Result=ChooseCard()
    player1.append(Card[Result])
for x in range(0,4):
    print(player1[x].GetNumber(), player1[x].GetColour())
