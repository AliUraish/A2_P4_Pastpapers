Animal=[]
Colour=[]
AnimalTopPointer=0
ColourTopPointer=0


def PushAnimal(data):
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer==20:
        return False
    else:
        Animal[AnimalTopPointer]=data
        AnimalTopPointer=AnimalTopPointer+1
        return True


def PopAnimal():
    global AnimalTopPointer
    global ColourTopPointer
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData=Animal[AnimalTopPointer-1]
        AnimalTopPointer=AnimalTopPointer-1
        return ReturnData
def ReadData():
    try:
        global AnimalTopPointer
        global ColourTopPointer
        File=open("AnimalData.txt","r")
        for line in File:
            PushAnimal(line)
        File.close()
    except:
        print("Could not find file")


def PushColour(data):
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer==10:
        return False
    else:
        Colour.append(data)
        ColourTopPointer+=1
        return True

def Popcolour():
    global AnimalTopPointer
    global ColourTopPointer
    if ColourTopPointer==0:
        return ""
    else:
        ReturnData=Colour[ColourTopPointer-1]
        ColourTopPointer=ColourTopPointer-1
        return ReturnData

def ReadData():
    try:
        global AnimalTopPointer
        global ColourTopPointer
        FileAnimal=open("AnimalData.txt","r")
        for line in FileAnimal:
            PushAnimal(line)
        FileAnimal.close()

        FileColour=open("ColourData.txt","r")
        for line in FileColour:
            PushColour(line)
        FileColour.close()
    except:
        print("Could not find file")



def OutputItem():
     global AnimalTopPointer
     global ColourTopPointer
     ColourReturned=Popcolour()
     AnimalReturned=PopAnimal()
     if ColourReturned=="":
        print("No colour")
        PushAnimal(AnimalReturned)
     else:
        if AnimalReturned=="":
            print("No animal")
            PushColour(ColourReturned)
        else:
            print(ColourReturned, AnimalReturned)


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
